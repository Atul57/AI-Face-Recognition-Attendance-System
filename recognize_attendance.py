import cv2
from deepface import DeepFace
from datetime import datetime
from database import get_connection
import time
import os

cap = cv2.VideoCapture(0)
marked = set()
start_time = time.time()
duration = 15  # seconds
DISTANCE_THRESHOLD = 0.4  # Adjust between 0.3 - 0.45 for strictness

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    elapsed = time.time() - start_time
    remaining = int(duration - elapsed)

    # Auto-close after 15 seconds
    if elapsed >= duration:
        print("15 seconds completed. Closing...")
        break

    try:
        result = DeepFace.find(
            img_path=frame,
            db_path="dataset",
            enforce_detection=False,
            silent=True
        )

        if len(result) > 0 and len(result[0]) > 0:
            # Filter only matches below the distance threshold
            df = result[0]
            confident_matches = df[df['distance'] < DISTANCE_THRESHOLD]

            if len(confident_matches) > 0:
                # Pick the best (lowest distance) confident match
                best_match = confident_matches.iloc[0]
                identity = best_match['identity']

                # Safely extract name from path
                name = os.path.basename(os.path.dirname(identity))

                # Display name on frame
                cv2.putText(frame, name, (30, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                # Mark attendance only once per person
                if name not in marked:
                    marked.add(name)
                    now = datetime.now()
                    date = now.strftime("%Y-%m-%d")
                    time_str = now.strftime("%H:%M:%S")

                    conn = get_connection()
                    cursor = conn.cursor()
                    cursor.execute(
                        "INSERT INTO attendance(student_name, date, time) VALUES(%s, %s, %s)",
                        (name, date, time_str)
                    )
                    conn.commit()
                    cursor.close()
                    conn.close()
                    print(f"Attendance marked: {name} at {time_str}")
            else:
                # No confident match found
                cv2.putText(frame, "Unknown", (30, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    except Exception as e:
        print("Error:", e)

    # Display countdown timer on frame
    cv2.putText(frame, f"Closing in: {remaining}s", (30, 90),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    cv2.imshow("AI Attendance System", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("Attendance session ended.")
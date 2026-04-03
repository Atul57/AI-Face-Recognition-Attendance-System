import cv2
import os

name = input("Enter student name: ")

folder = f"dataset/{name}"

if not os.path.exists(folder):
    os.makedirs(folder)

cap = cv2.VideoCapture(0)

count = 0

while True:

    ret, frame = cap.read()

    cv2.imshow("Capture Faces", frame)

    key = cv2.waitKey(1)

    if key == ord('c'):
        img_path = f"{folder}/{count}.jpg"
        cv2.imwrite(img_path, frame)
        print("Image saved:", img_path)
        count += 1

    if key == ord('q') or count >= 30:
        break

cap.release()
cv2.destroyAllWindows()
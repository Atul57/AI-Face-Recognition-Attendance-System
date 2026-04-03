import mysql.connector

def delete_record(student_name, date):

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Atul",
        database="attendance_system"
    )

    cursor = conn.cursor()

    query = """
    DELETE FROM attendance
    WHERE student_name = %s AND date = %s
    """

    cursor.execute(query, (student_name, date))

    conn.commit()

    print("Record deleted successfully")

    cursor.close()
    conn.close()


# Example
delete_record("Atul", "2026-03-15")
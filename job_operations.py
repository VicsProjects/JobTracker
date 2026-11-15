import sqlite3

def add_application(company, job_title, application_status, application_date, notes):
    connection = sqlite3.connect("jobs.db")
    cursor = connection.cursor()
    cursor.execute("""
    INSERT INTO applications(company, title, status, application_date, notes)
    VALUES (?, ?, ?, ?, ?)""", (company, job_title, application_status, application_date, notes)
    )

    connection.commit()
    connection.close()

def get_applications():
    connection = sqlite3.connect("jobs.db")
    cursor = connection.cursor()
    cursor.execute("""
    SELECT id, company, title, status, application_date, notes
    FROM applications
    ORDER BY application_date DESC""")
    applications = cursor.fetchall()
    connection.close()
    return applications

def update_application_status(application_id, new_status):
    connection = sqlite3.connect("jobs.db")
    cursor = connection.cursor()
    cursor.execute("""
    UPDATE applications
    SET status = ?
    WHERE id = ?""", (new_status, application_id))
    connection.commit()
    connection.close()

def delete_application(application_id):
    connection = sqlite3.connect("jobs.db")
    cursor = connection.cursor()
    cursor.execute("""
    DELETE FROM applications
    WHERE id = ?""", (application_id,))
    connection.commit()
    connection.close()
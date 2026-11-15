import sqlite3

def initialize_database():
    connection = sqlite3.connect("jobs.db")
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS applications(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company TEXT NOT NULL,
        title TEXT NOT NULL,
        status TEXT NOT NULL,
        application_date TEXT NOT NULL,
        notes TEXT
    )
    """)
    connection.commit()
    connection.close()
import sqlite3

db = 'admin_dashboard.db'

def db_connection():
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    return conn

def create_database():
    conn = db_connection()
    cursor = conn.cursor()

    conn.commit()
    conn.close()

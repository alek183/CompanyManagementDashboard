import sqlite3

db = 'admin_dashboard.db'

def db_connection():
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def create_database():
    conn = db_connection()
    cursor = conn.cursor()

    #Employees
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT UNIQUE,
            last_name TEXT UNIQUE
        )
    ''')

    #Clients
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            mail TEXT UNIQUE,
            contact_number TEXT
        )
    ''')

    #Tasks
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            status TEXT DEFAULT 'Pending',
            employee_id INTEGER,
            client_id INTEGER,
            creation_date TEXT,
            due_date TEXT,
            FOREIGN KEY (employee_id) REFERENCES employees(id),
            FOREIGN KEY (client_id) REFERENCES clients(id)
        )
    ''')

    #Stats
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT UNIQUE,
            total_tasks INTEGER DEFAULT 0,
            pending_tasks INTEGER DEFAULT 0,
            in_progress_tasks INTEGER DEFAULT 0,
            overdue_tasks INTEGER DEFAULT 0,
            completed_tasks INTEGER DEFAULT 0
        )
    ''')

    conn.commit()
    conn.close()

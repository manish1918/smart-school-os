import sqlite3

conn = sqlite3.connect("school.db")

cursor = conn.cursor()

# ---------------- USERS TABLE ----------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    password TEXT,
    role TEXT
)
""")

# ---------------- ATTENDANCE TABLE ----------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name TEXT,
    date TEXT,
    status TEXT
)
""")

# ---------------- HOMEWORK TABLE ----------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS homework (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT,
    title TEXT,
    description TEXT,
    due_date TEXT
)
""")

# ---------------- NOTES TABLE ----------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT,
    topic TEXT,
    content TEXT
)
""")

# ---------------- ANNOUNCEMENTS TABLE ----------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS announcements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    message TEXT
)
""")

# ---------------- FEES TABLE ----------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS fees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name TEXT,
    amount TEXT,
    status TEXT
)
""")
# ---------------- SAVE ----------------

conn.commit()

# ---------------- CLOSE ----------------

conn.close()

print("Database Ready 🚀")
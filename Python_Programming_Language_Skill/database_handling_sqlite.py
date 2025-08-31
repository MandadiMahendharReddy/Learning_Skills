import sqlite3

# Connect to SQLite DB (creates file if not exists)
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    marks INTEGER
)
""")

# Insert Data
cursor.execute("INSERT INTO students (name, marks) VALUES (?, ?)", ("Krishna", 95))
conn.commit()

# Fetch Data
cursor.execute("SELECT * FROM students")
print(cursor.fetchall())

conn.close()



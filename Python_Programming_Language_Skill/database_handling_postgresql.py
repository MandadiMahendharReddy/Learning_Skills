import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="mydb_post",
    user="mahendhar",
    password="password",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id SERIAL PRIMARY KEY,
    name TEXT,
    salary INT
)
""")

# Insert Data
cursor.execute("INSERT INTO employees (name, salary) VALUES (%s, %s)", ("Arjun", 50000))
conn.commit()

# Fetch Data
cursor.execute("SELECT * FROM employees")
print(cursor.fetchall())

conn.close()

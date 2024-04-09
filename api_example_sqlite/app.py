from fastapi import FastAPI, HTTPException
import sqlite3

app = FastAPI()

# Create SQLite database connection
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
conn.commit()

@app.get('/get_data')
def get_data():
    # Retrieve data from the SQLite database
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    if rows:
        return [{'id': row[0], 'name': row[1], 'age': row[2]} for row in rows]
    else:
        return []

@app.post('/post_data')
def post_data(name: str, age: int):
    # Insert data into the SQLite database
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    return {'message': 'Data inserted successfully'}

# Close the database connection when the application stops
@app.on_event("shutdown")
def shutdown_event():
    conn.close()

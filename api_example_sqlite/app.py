from fastapi import FastAPI, HTTPException
import sqlite3

app = FastAPI()

# Create SQLite database connection (moved inside the route functions)
def get_connection():
    return sqlite3.connect('example.db')

@app.get('/get_data')
def get_data():
    # Create a new connection and cursor for each request
    conn = get_connection()
    cursor = conn.cursor()

    # Retrieve data from the SQLite database
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    data = [{'id': row[0], 'name': row[1], 'age': row[2]} for row in rows]
    
    # Close the cursor and connection
    cursor.close()
    conn.close()

    return data

@app.post('/post_data')
def post_data(name: str, age: int):
    # Create a new connection and cursor for each request
    conn = get_connection()
    cursor = conn.cursor()

    # Insert data into the SQLite database
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    return {'message': 'Data inserted successfully'}

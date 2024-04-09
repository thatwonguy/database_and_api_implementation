from fastapi import FastAPI, HTTPException
import sqlite3

app = FastAPI()

# Create SQLite database connection (moved inside the route functions)
def get_connection():
    return sqlite3.connect('example.db')

# Create the 'example' table if it doesn't exist
conn = get_connection()
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS example
                (name TEXT, age INTEGER)''')

@app.get('/get_data')
def get_data():
    # Create a new connection and cursor for each request
    conn = get_connection()
    cursor = conn.cursor()

    # Retrieve data from the SQLite database
    cursor.execute("SELECT * FROM example")
    rows = cursor.fetchall()
    
    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Check if there are rows, then return the data
    if rows:
        return [{'name': row[0], 'age': row[1]} for row in rows]
    else:
        return []

@app.post('/post_data')
def post_data(data: dict):
    name = data.get('name')
    age = data.get('age')
    if not name or not age:
        raise HTTPException(status_code=400, detail="Name and age are required")

    # Create a new connection and cursor for each request
    conn = get_connection()
    cursor = conn.cursor()

    # Insert data into the SQLite database
    cursor.execute("INSERT INTO example (name, age) VALUES (?, ?)", (name, age))
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    return {'message': 'Data inserted successfully'}

# run this app with the following in terminal after making sure you are in the directory in your CLI-->  uvicorn app:app --reload
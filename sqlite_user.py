import sqlite3
import hashlib

# Connect to the SQLite database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create a users table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT UNIQUE,
                    password TEXT
                )''')

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to register a new user
def register_user(username, password):
    hashed_password = hash_password(password)
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
    conn.commit()
    print('User registered successfully!')

# Function to login a user
def login_user(username, password):
    hashed_password = hash_password(password)
    cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, hashed_password))
    user = cursor.fetchone()
    if user:
        print('Login successful!')
    else:
        print('Invalid username or password.')

# Register a new user (uncomment to test)
# register_user('testuser', 'testpassword')

# Login a user (uncomment to test)
# login_user('testuser', 'testpassword')

# Close the database connection
conn.close()

import requests

# Base URL for the FastAPI server
BASE_URL = 'http://localhost:8000'

# Post data to the SQLite database
def post_data(name: str, age: int):
    payload = {'name': name, 'age': age}
    response = requests.post(f'{BASE_URL}/post_data', json=payload)
    if response.status_code == 200:
        print("Data posted successfully")
    else:
        print(f"Failed to post data. Status code: {response.status_code}")

# Get data from the SQLite database
def get_data():
    response = requests.get(f'{BASE_URL}/get_data')
    if response.status_code == 200:
        data = response.json()
        print("Data from database:")
        for entry in data:
            print(f"Name: {entry['name']}, Age: {entry['age']}")
    else:
        print(f"Failed to get data. Status code: {response.status_code}")

# Test the endpoints
if __name__ == '__main__':
    # Post data
    print("Posting data to the database:")
    post_data('Johnny', 35)

    # Get data
    print("\nGetting data from the database:")
    get_data()

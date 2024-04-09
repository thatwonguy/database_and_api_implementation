import requests

# Define the base URL of the FastAPI app
BASE_URL = 'http://localhost:8000'

# Function to get data from the /get_data endpoint
def get_data():
    response = requests.get(f'{BASE_URL}/get_data')
    if response.status_code == 200:
        return response.json()
    else:
        print('Error:', response.text)
        return None

# Function to post data to the /post_data endpoint
def post_data(data):
    response = requests.post(f'{BASE_URL}/post_data', json=data)
    if response.status_code == 200:
        print('Data posted successfully')
    else:
        print('Error:', response.text)

# Example usage
if __name__ == '__main__':
    # Get data from the API
    print(get_data())

    # Post data to the API
    post_data({'name': 'Alice', 'age': 25})

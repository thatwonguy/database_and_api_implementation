from fastapi import FastAPI

app = FastAPI()

@app.get('/get_data')
def get_data():
    # Logic to retrieve data from the database
    data = {'name': 'John', 'age': 30}
    return data

@app.post('/post_data')
def post_data(data: dict):
    # Logic to receive and process data from the client
    # Process the data...
    return {'message': 'Data received successfully'}

# to run this type the following in terminal --> uvicorn app:app --reload
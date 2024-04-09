# sqlite_implementation
Demo on how to utilize sqlite as a database, which can mimic a cloud-based database.

- it is a serverless database that holds the data outside of memory but not on the cloud
- `sqlite_user.py` is a standalone file example to demonstrate usage of sqlite
- `api_example` is an folder containing two python scripts that use api calls to tap into each other
     - `app.py` is a python file that allows for **GET** and **POST** requests
     - `client.py` is another python file that would allow a separate user to tap into those endpoints and carry out **GET** and **POST** requests

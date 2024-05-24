[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# sqlite_implementation

- ### Demo on how to utilize sqlite as a database, which can mimic a cloud-based database.

- ### Demo on usage of fastapi to utilize endpoints for end-users to tap into data.
---
- ### PREREQUISITES
     - ensure that you pip install all required libraries
     - see the included `requirements.txt` file in the repo for a list of all libraries needed. You can install them individually or simply type the following in your IDE bash terminal:
     ```
     pip install -r requirements.txt
     ```
> [!NOTE]
> Ideally you want to create a virtual environment(venv) for the individual project you are working on and install all the requirements inside the venv after activating it in your terminal to avoid package installation issues with other projects.
> Alternatively, a docker/ kubernetes implementation would be even more powerful for production settings.
> 
---
Sqlite is a serverless database that holds the data outside of memory but not on the cloud.
1. `sqlite_user.py` is a standalone file example to demonstrate usage of sqlite
2. `api_example_in_memory` is a folder containing two separate python scripts that use api calls to tap into each other
     - `app.py` is a python file that allows for **GET** and **POST** requests
     - `client.py` is another python file that would allow a separate user to tap into those endpoints and carry out **GET** and **POST** requests

          1. to run the above scripts in local you need to type the following in your terminal to get the `app.py` started

          ```
          uvicorn app:app --reload
          ```

          Here's what each part of the command does:

          - **uvicorn**: This is the command to run the ASGI server.
          - **app:app**: This specifies the module and the variable within that module where the FastAPI app is defined. In this case, app refers to the variable name holding the FastAPI app within the app.py module.
          - **--reload**: This option tells uvicorn to automatically reload the server whenever the source code changes. 

          It's useful during development to see changes immediately without restarting the server manually.
          Make sure to replace app with the appropriate variable name if you've named it differently in your app.py file.

          After running this command, you'll see output indicating that the FastAPI app is running, and you can access it at the localhost and port number you specified.

          To see that the data posted, type the following in your URL if your URL is https:localhost:8000:
          ```
          http://localhost:8000/get_data
          ```
          - if you followed this example you should see:
          > {"name":"John","age":30}

---
- ### Below is a demo of how to put *sqlite* and *fastapi* together now.
---

The above examples of sqlite and fastapi shown with the files should provide good foundational knowledge on how sqlite and fastapi works. The next step would be to change the `app.py` script to point to a sqlitedb instead of in-memory data.

With this modification you can save the data in a database and allow the end user access to the data via an API instead of direct access to the database.

3. `api_example_sqlite` is a folder that uses sqlite and fastapi, bringing examples 1 and 2 together. 
     - this api and sqlite implementation only has `post` and `get` functionality and adding additional functionalities (deletion of data rows) can be added and incorporated. Modify as you see fit for your use-case!
     - `app.py` is initiated by typing the following to start the localhost and create the db and allowing the api-endpoints to be up and running:
     ```
     uvicorn app:app --reload
     ```
     - `client.py` is then run with the following code to interact with `app.py` using the api-endpoints for get and post:
     ```
     python client.py
     ```

---
- ### Below is a demo of how to put *sqlalchemy* and *fastapi* together now.
---

Here we use sqlalchemy instead of sqlite. It is a much more robust python library than just a simple serverless sqlitedb. We modify the `app.py` file to utilize class objects to create the database and api layer and then we modify the `client.py` file to mimic an end-user connecting to it. 

With this modification you can save the data in a database and allow the end user access to the data via an API instead of direct access to the database.

4. `api_example_sqlalchemy` is a folder that uses sqlalchemy and fastapi, improving on example 3 above. 
     - this api and sqlalchemy implementation only has `post` and `get` functionality and adding additional functionalities (deletion of data rows) can be added and incorporated. Modify as you see fit for your use-case!
     - `app.py` is initiated by typing the following to start the localhost and create the db and allowing the api-endpoints to be up and running:
     ```
     uvicorn app:app --reload
     ```
     - `client.py` is then run with the following code to interact with `app.py` using the api-endpoints for get and post:
     ```
     python client.py
     ```

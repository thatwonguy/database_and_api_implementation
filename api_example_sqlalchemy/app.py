from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()

# Define SQLAlchemy models
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)

# Connect to the SQLite database using SQLAlchemy
SQLALCHEMY_DATABASE_URL = "sqlite:///./example.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create database tables
Base.metadata.create_all(bind=engine)

@app.get('/get_data')
def get_data():
    # Create a new database session
    db = SessionLocal()
    users = db.query(User).all()
    db.close()
    return users

@app.post('/post_data')
def post_data(data: dict):
    name = data.get('name')
    age = data.get('age')
    if not name or not age:
        raise HTTPException(status_code=400, detail="Name and age are required")
    
    # Create a new database session
    db = SessionLocal()
    user = User(name=name, age=age)
    db.add(user)
    db.commit()
    db.close()
    return {'message': 'Data inserted successfully'}

# to run this type the following in terminal --> uvicorn app:app --reload
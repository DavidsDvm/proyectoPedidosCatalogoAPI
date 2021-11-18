import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = os.getenv('CONNECTION_STRING', 'postgresql://wsjcdinaxlylzy:fa53f75b33ccbf0c6b04e6e9902f6edddf21ded89b08d6c6d2c01c9d9e0e5c68@ec2-3-209-38-221.compute-1.amazonaws.com:5432/dfdeoik7h3qvuf')

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()
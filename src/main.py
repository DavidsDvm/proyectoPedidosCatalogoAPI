from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .schemas import CreateUserRequest
from .database import get_db
from .models import User
import uvicorn
import os

app = FastAPI()

@app.get("/")
def root():
    return [{"message": "Hello World", "status": "ok"}]

@app.get("/api/user/all")
def getUsers(db: Session = Depends(get_db)):
    all_users = db.query(User).all()
    all_data = []
    for user in all_users:
        data = {}
        data["id"]=user.id
        data["email"]=user.user_email
        data["password"]=user.user_passwordvarchar
        data["name"]=user.user_namevarchar
        all_data.append(data)
    return all_data

@app.get("/api/user/{email}")
def searchUserByEmail(email: str, db: Session = Depends(get_db)):
    userExist = db.query(User).filter(User.user_email == email).first()
    if userExist:
        return 'True'
    else:
        return 'False'

@app.get("/api/user/{email}/{password}")
def searchUserByCredentials(email: str, password: str ,db: Session = Depends(get_db)):
    userExist = db.query(User).filter(User.user_email == email and User.user_passwordvarchar == password).first()
    if userExist:
        data = {}
        data["id"]=userExist.id
        data["email"]=userExist.user_email
        data["password"]=userExist.user_passwordvarchar
        data["name"]=userExist.user_namevarchar
        return data
    else:
        data = {}
        data["id"]=None
        data["email"]=email
        data["password"]=password
        data["name"]="NO DEFINIDO"
        return data

@app.post("/api/user/new", status_code=201)
def newUser(details: CreateUserRequest, db: Session = Depends(get_db)):
    print("Si corrio")
    to_create = User(details.email, details.name, details.password)
    db.add(to_create)
    db.commit()
    return []

if __name__ == "__main__":

    port = int(os.environ.get('PORT', 5000))

    uvicorn.run(app, host="0.0.0.0", port=port, log_level="info")
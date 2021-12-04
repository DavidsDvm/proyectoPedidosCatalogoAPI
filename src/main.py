from fastapi import FastAPI, Depends, Response, status
from sqlalchemy.orm import Session
from .schemas import CreateUserRequest, CreateCookwareRequest
from .database import get_db
from .models import User, Cookware
from datetime import datetime
import uvicorn
import os

app = FastAPI()

# General API start point

@app.get("/")
def root():
    return [{"message": "Hello World", "status": "ok"}]

# User API -- GET methods

@app.get("/api/user/all")
def getUsers(db: Session = Depends(get_db)):
    all_users = db.query(User).all()
    all_data = []
    for user in all_users:
        data = {}
        data["id"]=user.id
        data["identification"] = user.user_identification
        data["name"] = user.user_namevarchar
        data["birthtDay"] = (str(user.user_birthday)).replace(" ", "T") + ".000+00:00"
        data["monthBirthtDay"] = user.user_monthBirthday
        data["address"] = user.user_address
        data["cellPhone"] = user.user_cellphone
        data["email"] = user.user_email
        data["password"] = user.user_passwordvarchar
        data["zone"] = user.user_zone
        data["type"] = user.user_type
        all_data.append(data)
    return all_data

@app.get("/api/user/{id}")
def getUserById(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if user:
        data = {}
        data["id"]=user.id
        data["identification"] = user.user_identification
        data["name"] = user.user_namevarchar
        data["birthtDay"] = (str(user.user_birthday)).replace(" ", "_") + ".000+00:00"
        data["monthBirthtDay"] = user.user_monthBirthday
        data["address"] = user.user_address
        data["cellPhone"] = user.user_cellphone
        data["email"] = user.user_email
        data["password"] = user.user_passwordvarchar
        data["zone"] = user.user_zone
        data["type"] = user.user_type
        return data

@app.get("/api/user/emailexist/{email}")
def searchUserByEmail(email: str, db: Session = Depends(get_db)):
    userExist = db.query(User).filter(User.user_email == email).first()
    if userExist:
        return 'True'
    else:
        return 'False'

@app.get("/api/user/{email}/{password}")
def searchUserByCredentials(email: str, password: str ,db: Session = Depends(get_db)):
    userExist = db.query(User).filter(User.user_email == email, User.user_passwordvarchar == password).first()
    print(userExist)
    if userExist:
        data = {}
        data["id"]=userExist.id
        data["identification"] = userExist.user_identification
        data["name"]= userExist.user_namevarchar
        data["birthtDay"] = str(userExist.user_birthday) + ".000+00:00"
        data["monthBirthtDay"] = userExist.user_monthBirthday
        data["address"] = userExist.user_address
        data["cellPhone"] = userExist.user_cellphone
        data["email"] = userExist.user_email
        data["password"] = userExist.user_passwordvarchar
        data["zone"] = userExist.user_zone
        data["type"] = userExist.user_type
        return data
    else:
        data = {}
        data["id"] = None
        data["identification"] = None
        data["name"]= None
        data["birthtDay"] = None
        data["monthBirthtDay"] = None
        data["address"] = None
        data["cellPhone"] = None
        data["email"] = None
        data["password"] = None
        data["zone"] = None
        data["type"] = None
        return data

# User API -- POST methods

@app.post("/api/user/new", status_code=201)
def newUser(details: CreateUserRequest, db: Session = Depends(get_db)):
    dateBirthday = (str(details.birthtDay)).split('+')[0]
    dateBirthdayAdd = datetime.strptime(dateBirthday, '%Y-%m-%d %H:%M:%S')

    to_create = User(details.id, details.identification, details.name, dateBirthdayAdd, details.monthBirthtDay, details.address, details.cellPhone, details.email, details.password, details.zone, details.type)
    db.add(to_create)
    db.commit()
    return []

# User API -- PUT methods

@app.put("/api/user/update", status_code=201)
def updateUser(details: CreateUserRequest, response: Response, db: Session = Depends(get_db)):
    to_update = db.query(User).filter(User.id == details.id).first()
    if to_update:
        to_update.user_identification = details.identification
        to_update.user_namevarchar = details.name
        to_update.user_birthday = details.birthtDay
        to_update.user_monthBirthday = details.monthBirthtDay
        to_update.user_address = details.address
        to_update.user_cellphone = details.cellPhone
        to_update.user_email = details.email
        to_update.user_passwordvarchar = details.password
        to_update.user_zone = details.zone
        to_update.user_type = details.type
        db.commit()
        return []
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return []

# User API -- DELETE methods

@app.delete("/api/user/{id}", status_code=204)
def deleteUser(id: int, response: Response, db: Session = Depends(get_db)):
    to_delete = db.query(User).filter(User.id == id).first()
    if to_delete:
        db.delete(to_delete)
        db.commit()
        return []
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return []

# Cookware API -- GET methods

@app.get("/api/cookware/all")
def getCookware(db: Session = Depends(get_db)):
    all_cookware = db.query(Cookware).all()
    all_data = []
    for cookware in all_cookware:
        data = {}
        data["reference"] = cookware.cookware_reference
        data["brand"] = cookware.cookware_brand
        data["category"]= cookware.cookware_category
        data["materiales"] = cookware.cookware_material
        data["dimensiones"] = cookware.cookware_dimentions
        data["description"] = cookware.cookware_description
        data["availability"] = cookware.cookware_availability
        data["price"] = cookware.cookware_price
        data["quantity"] = cookware.cookware_quantity
        data["photography"] = cookware.cookware_photo
        all_data.append(data)
    return all_data

# Cookware API -- POST methods

@app.post("/api/cookware/new", status_code=201)
def newCookware(details: CreateCookwareRequest, db: Session = Depends(get_db)):
    to_create = Cookware(details.reference, details.brand, details.category, details.materiales, details.dimensiones, details.description, details.availability, details.price, details.quantity, details.photography)
    db.add(to_create)
    db.commit()
    return []

# Cookware API -- PUT methods

@app.put("/api/cookware/update", status_code=201)
def updateCookware(details: CreateCookwareRequest, response: Response, db: Session = Depends(get_db)):
    to_update = db.query(Cookware).filter(Cookware.cookware_reference == details.reference).first()
    if to_update:
        to_update.cookware_reference = details.reference
        to_update.cookware_brand = details.brand
        to_update.cookware_category = details.category
        to_update.cookware_material = details.materiales
        to_update.cookware_dimentions = details.dimensiones
        to_update.cookware_description = details.description
        to_update.cookware_availability = details.availability
        to_update.cookware_price = details.price
        to_update.cookware_quantity = details.quantity
        to_update.cookware_photo = details.photography
        db.commit()
        return []
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return []

# cookware API -- DELETE methods

@app.delete("/api/cookware/{reference}", status_code=204)
def deleteCookware(reference: str, response: Response, db: Session = Depends(get_db)):
    to_delete = db.query(Cookware).filter(Cookware.cookware_reference == reference).first()
    if to_delete:
        db.delete(to_delete)
        db.commit()
        return []
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return []

# Run the server

if __name__ == "__main__":

    port = int(os.environ.get('PORT', 5000))

    uvicorn.run(app, host="0.0.0.0", port=port, log_level="info")
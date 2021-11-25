from sqlalchemy import Integer, String, Boolean, Float
from sqlalchemy.sql.schema import Column
from .database import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    user_identification = Column(String(50), unique=True, nullable=False)
    user_namevarchar = Column(String(80), nullable=False)
    user_address = Column(String(80), nullable=False)
    user_cellphone = Column(String(20), nullable=False)
    user_email = Column(String(50), nullable=False, unique=True)
    user_passwordvarchar = Column(String(50), nullable=False)
    user_zone = Column(String(20), nullable=False)
    user_type = Column(String(20), nullable=False)

    def __init__(self, user_identification, user_namevarchar, user_address, user_cellphone, user_email, user_passwordvarchar, user_zone, user_type):
        self.user_identification = user_identification
        self.user_namevarchar = user_namevarchar
        self.user_address = user_address
        self.user_cellphone = user_cellphone
        self.user_email = user_email
        self.user_passwordvarchar = user_passwordvarchar
        self.user_zone = user_zone
        self.user_type = user_type

class Cookware(Base):
    __tablename__ = 'cookware'

    id = Column(Integer, primary_key=True)
    cookware_reference = Column(String(50), nullable=False)
    cookware_brand = Column(String(150), nullable=False)
    cookware_category = Column(String(150), nullable=False)
    cookware_material = Column(String(250), nullable=False)
    cookware_dimentions = Column(String(100), nullable=False)
    cookware_description = Column(String(250), nullable=False)
    cookware_availability = Column(Boolean, nullable=False)
    cookware_price = Column(Float, nullable=False)
    cookware_quantity = Column(Integer, nullable=False)
    cookware_photo = Column(String(255), nullable=False)

    def __init__(self, cookware_reference, cookware_brand, cookware_category, cookware_material, cookware_dimentions, cookware_description, cookware_availability, cookware_price, cookware_quantity, cookware_photo):
        self.cookware_reference = cookware_reference
        self.cookware_brand = cookware_brand
        self.cookware_category = cookware_category
        self.cookware_material = cookware_material
        self.cookware_dimentions = cookware_dimentions
        self.cookware_description = cookware_description
        self.cookware_availability = cookware_availability
        self.cookware_price = cookware_price
        self.cookware_quantity = cookware_quantity
        self.cookware_photo = cookware_photo
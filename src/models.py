from sqlalchemy import Integer, String, Boolean, Float, DateTime 
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column, ForeignKey, Table
from .database import Base

# Many to many realation beetween User and Order
class UserAndOrder(Base):
    __tablename__ = 'user_and_order'

    user_id = Column(ForeignKey('user.id'), primary_key=True)
    order_id = Column(ForeignKey('order.id'), primary_key=True)

    # Realtions
    user = relationship("User", back_populates="userOrder")
    order = relationship("Order", back_populates="orderUser")

    def __init__(self, user_id, order_id):
        self.user_id = user_id
        self.order_id = order_id

class User(Base):
    __tablename__ = 'user'

    # primary key
    id = Column(Integer, primary_key=True, autoincrement=False)
    
    # fields of the table
    user_identification = Column(String(50), unique=True, nullable=False)
    user_namevarchar = Column(String(80), nullable=False)
    user_birthday = Column(DateTime, nullable=False)
    user_monthBirthday = Column(String(20), nullable=False)
    user_address = Column(String(80), nullable=False)
    user_cellphone = Column(String(20), nullable=False)
    user_email = Column(String(50), nullable=False, unique=True)
    user_passwordvarchar = Column(String(50), nullable=False)
    user_zone = Column(String(20), nullable=False)
    user_type = Column(String(20), nullable=False)

    # foreign keys
    userOrder = relationship("UserAndOrder", back_populates="user")

    def __init__(self, id, user_identification, user_namevarchar, user_birthday, user_monthBirthday,user_address, user_cellphone, user_email, user_passwordvarchar, user_zone, user_type):
        self.id = id
        self.user_identification = user_identification
        self.user_namevarchar = user_namevarchar
        self.user_birthday = user_birthday
        self.user_monthBirthday = user_monthBirthday
        self.user_address = user_address
        self.user_cellphone = user_cellphone
        self.user_email = user_email
        self.user_passwordvarchar = user_passwordvarchar
        self.user_zone = user_zone
        self.user_type = user_type

# Many to many relation beetween Cookware and Order
class CookwareAndOrder(Base):
    __tablename__ = 'cookware_and_order'

    cookware_reference = Column(ForeignKey('cookware.cookware_reference'), primary_key=True)
    order_id = Column(ForeignKey('order.id'), primary_key=True)
    order_quantity = Column(Integer, nullable=True)

    # Realtions
    cookware = relationship("Cookware", back_populates="cookwareOrder")
    order = relationship("Order", back_populates="orderCookware")

    def __init__(self, cookware_reference, order_id, order_quantity):
        self.cookware_reference = cookware_reference
        self.order_id = order_id
        self.order_quantity = order_quantity

class Cookware(Base):
    __tablename__ = 'cookware'

    # primary key
    cookware_reference = Column(String(50), primary_key=True, autoincrement=False)

    # fields of the table
    cookware_brand = Column(String(150), nullable=False)
    cookware_category = Column(String(150), nullable=False)
    cookware_material = Column(String(250), nullable=False)
    cookware_dimentions = Column(String(100), nullable=False)
    cookware_description = Column(String(250), nullable=False)
    cookware_availability = Column(Boolean, nullable=False)
    cookware_price = Column(Float, nullable=False)
    cookware_quantity = Column(Integer, nullable=False)
    cookware_photo = Column(String(255), nullable=False)

    # foreign keys
    cookwareOrder = relationship("CookwareAndOrder", back_populates="cookware")

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

class Order(Base):
    __tablename__ = 'order'
    
    # primary key
    id = Column(Integer, primary_key=True, autoincrement=False)
    
    # fields of the table
    order_register = Column(DateTime, nullable=False)
    order_status = Column(String(50), nullable=False)

    # foreign keys
    orderUser = relationship("UserAndOrder", back_populates="order")
    orderCookware = relationship("CookwareAndOrder", back_populates="order")
    
    def __init__(self, id, order_register, order_status):
        self.id = id
        self.order_register = order_register
        self.order_status = order_status
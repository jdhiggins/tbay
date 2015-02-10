from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Table, ForeignKey, Column, Float, Integer, String, DateTime

engine = create_engine('postgresql://action:action@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
"""
pizza_topping_table = Table('pizza_topping_association', Base.metadata,
                         Column('pizza_id', Integer, ForeignKey('pizza.id')),
                         Column('topping_id', Integer, ForeignKey('topping.id'))
                            )

class Pizza(Base):
    __tablename__ = 'pizza'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    toppings = relationship("Topping", secondary="pizza_topping_association",
                          backref="pizzas")
                            
                            
class Topping(Base):
    __tablename__ = 'topping'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

item_user_table = Table

item to user is one to one
item to bid is one to many
user to bids is one to many
"""

class Item(Base):
    __tablename__ = "items"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)

    bids = relationship("Bid", backref="item")
    
    owner_id = Column(Integer, ForeignKey('users.id'), nullable=False)
        
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)

    items = relationship("Item", backref="owner")
    
    bids = relationship("Bid", backref="owner")
    
class Bid(Base):
    __tablename__ = "bids"
    
    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)

    owner_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
    


Base.metadata.create_all(engine)

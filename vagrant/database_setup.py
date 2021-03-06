import os
import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()
### Everything above goes in the beginning


class Restaurant(Base):
	__tablename__ = 'restaurant'

	id = Column(Integer, primary_key = True)
	name = Column(String(80), nullable = False)

class MenuItem(Base):
	__tablename__ = 'menu_item'
	
	id = Column(Integer, primary_key = True)
	name = Column(String(80), nullable = False)
	description = Column(String(80), nullable = False)
	course = Column(String(250))
	price = Column(String(8))
	restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
	restaurant = relationship(Restaurant)


#######insert at end of file #########

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)

#!/usr/bin/python3
"""[class definition of a city and an instance Base = declarative_base()]
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State

# declarative class
Base = declarative_base()


class City(Base):
    """[ class definition of a City]

    Args:
        Base ([Integer, String]):
        [ Class base that recive a integer and strings ]
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

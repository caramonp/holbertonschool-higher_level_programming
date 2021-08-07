#!/usr/bin/python3
"""[class definition of a State and an instance Base = declarative_base()]
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# declarative class
Base = declarative_base()


class State(Base):
    """[ class definition of a State]

    Args:
        Base ([Integer, String]):
        [ Class base that recive a integer and strings ]
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

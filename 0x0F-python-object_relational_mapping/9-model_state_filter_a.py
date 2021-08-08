#!/usr/bin/python3
"""[script that lists all State objects that contain
    the letter a from the database hbtn_0e_6_usa]
"""

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'

    engine = create_engine(url.format(user, password, db),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    for states in session.query(State).filter(State.name.
                                              like('%a%')).order_by(State.id):
        print("{}: {}".format(states.id, states.name))

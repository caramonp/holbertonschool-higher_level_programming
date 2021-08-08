#!/usr/bin/python3
"""[script that lists all State objects that pass an argument
    from the database hbtn_0e_6_usa]
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

    Base.metadata.create_all(engine)

    states = session.query(State).\
        filter(State.name == sys.argv[4]).order_by(State.id).all()

    if states:
        print("{}".format(states[0].id))
    else:
        print("Not found")
    session.close()

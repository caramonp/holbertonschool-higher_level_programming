#!/usr/bin/python3
"""[script that changes the name of a State object
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
    Session.configure(bind=engine)
    session = Session()

    states = session.query(State).filter(State.id == 2).first()
    states.name = 'New Mexico'

    session.commit()
    session.close()

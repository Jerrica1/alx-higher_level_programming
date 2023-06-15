#!/usr/bin/python3
"""
This module is designed to find all states that contain the letter 'a'
and delete them from the db
"""

from sys import argv
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy import update


if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}',
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    delete_states = session.query(State).filter(State.name.like('%a%'))
    for match in delete_states:
        session.delete(match)
    session.commit()
    session.close()

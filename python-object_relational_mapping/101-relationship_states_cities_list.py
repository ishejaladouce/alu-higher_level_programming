#!/usr/bin/python3
"""
Lists all State objects and corresponding City objects from the database.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from relationship_state import State
from relationship_city import City
from sqlalchemy.orm import scoped_session


def main():
    """Connects to the database and lists all states and their cities"""
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    url = f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}"

    # Create engine and session
    engine = create_engine(url, pool_pre_ping=True)
    Session = scoped_session(sessionmaker(bind=engine))
    session = Session()

    # Query all states with joined cities, sorted by state.id and city.id
    states = session.query(State).options(joinedload(State.cities)).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")
        sorted_cities = sorted(state.cities, key=lambda city: city.id)
        for city in sorted_cities:
            print(f"\t{city.id}: {city.name}")

    session.close()


if __name__ == "__main__":
    main()

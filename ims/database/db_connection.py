from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool


# The class which represents the BMI database
# It is responsible for creating and closing sessions
class DatabaseConnection:
    # the sqlalchemy base class which the table classes will inherit
    Base = declarative_base()

    # the engine and session maker are made static so that only one of them needs to be created
    # creates the engine for the database
    # sample_bmi.db should be changed to something more realistic
    # NullPool pool class is equivalent to no connection pool
    # Should be adapted to postgres SQL
    engine = create_engine('sqlite:///sample_bmi.db', poolclass=NullPool)

    # creates a session maker for creating sessions
    session_maker = sessionmaker(bind=engine)

    # creates all tables if not present
    def __init__(self):
        DatabaseConnection.Base.metadata.create_all(DatabaseConnection.engine)

    def __enter__(self):
        self.session = DatabaseConnection.session_maker()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

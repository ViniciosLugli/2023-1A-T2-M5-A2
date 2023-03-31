from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base


# Create the engine for the database
engine = create_engine('sqlite:///database.db')

# Create the tables
Base.metadata.create_all(engine)

# Create the session
Session = sessionmaker(bind=engine)

# Instantiate the session
session = Session()

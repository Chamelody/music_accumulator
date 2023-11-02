import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQL_URI = os.getenv("SQL_URI")

engine = create_engine(SQL_URI, echo=True)  # echo True is development mode.
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

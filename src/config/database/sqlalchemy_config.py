from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("sqlite:///test.db", echo=True)  # echo True is development mode.
Base = declarative_base()

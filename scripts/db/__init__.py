from sqlalchemy import create_engine
from config import Config
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

config = Config()
engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

from db import models
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

URL = "sqlite:///jobs.db"

engine = create_engine(
    URL, connect_args={"check_same_thread": False}
)

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

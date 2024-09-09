from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./todo.db"
engine = create_engine(DATABASE_URL,connect_args={"check_same_thread":False})

Base = declarative_base()

SessionLocal = sessionmaker(autoflush=False,autocommit=False, bind=engine)
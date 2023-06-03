from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
import time

def create_session(SQLALCHEMY_DATABASE_URL: str):
    while True:
        try:
            engine = create_engine(SQLALCHEMY_DATABASE_URL)
            session_local = sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=engine,
            )
            return engine, session_local
        except OperationalError:
            print("Database connection failed. Retrying in 5 seconds...")
            time.sleep(5)

SQLALCHEMY_DATABSE_URL = "postgresql://wakandata:wakandata@postgres/mlopsvn-marathon"
engine, session_local = create_session(SQLALCHEMY_DATABSE_URL)
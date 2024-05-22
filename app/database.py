from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import settings

# postgresql://<username>:<password>@<host>[:<port>]/<database>
SQLALCHEMY_DB_URL = (
    "postgresql://{db_uname}:{db_pwd}@{db_host}:{db_port}/{db_name}".format(
        db_uname=settings.database_username,
        db_pwd=settings.database_password,
        db_host=settings.database_hostname,
        db_port=settings.database_port,
        db_name=settings.database_name,
    )
)

engine = create_engine(SQLALCHEMY_DB_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


"""
PostgreSQL database driver for python, in case 
you want to run SQL queries instead of ORM

import psycopg2
from psycopg2.extras import RealDictCursor


try:
    conn = psycopg2.connect(
        host="localhost",
        database="fastapi",
        user="postgres",
        password="shanky123",
        cursor_factory=RealDictCursor,
    )
    cursor = conn.cursor()
    print("Database connection successful!")
except Exception as err:
    print("Connection to database failed")
    print("Error: ", err)
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://root:root123@localhost/employee_system"

engine = create_engine(DATABASE_URL) #connects Python to MySQL

SessionLocal = sessionmaker(bind=engine) #used to interact with DB

Base = declarative_base() #used to define table models
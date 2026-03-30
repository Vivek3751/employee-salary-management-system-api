from sqlalchemy import Column, Integer, String, Float
from database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    department = Column(String(100))
    base_salary = Column(Float)
    rating = Column(Integer)
    bonus = Column(Float)
    total_salary = Column(Float)

'''
This class = your SQL table
This maps your MySQL table to Python class.

SQL Column	Python
name	    Column(String)
salary	    Column(Float)
'''

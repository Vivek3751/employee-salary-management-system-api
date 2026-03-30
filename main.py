from fastapi import FastAPI, Depends   # FastAPI framework + Depends for dependency injection without 'Depends' no 'def' function will be runned.
#from pydantic import BaseModel 
from sqlalchemy.orm import Session     # Session is used to talk to database
from database import engine, SessionLocal   # Import DB connection and session
import models                          # Import our table (Employee class)
from schemas import EmployeeCreate     # Import request validation schema

# Create FastAPI app instance
app = FastAPI()
# This creates tables in database if they don't exist
models.Base.metadata.create_all(bind=engine)

# Dependency function to get DB session -- In simple for 'Database connection'
def get_db():
    db = SessionLocal()   # Create a new database session or Open DB connection
    try:
        yield db          # Give DB session to API
    finally:
        db.close()        # Close DB connection after request is done

#Request Body Model
# class Employee(BaseModel):
#     name:str
#     department: str
#     base_salary: float
#     rating: int

# Simple GET API (home)
@app.get("/")
def home():
    return {"message": "Employee System API Running"}

#POST API To create employee  -- CREATE Operation
@app.post("/employees")
def create_employee(emp: EmployeeCreate, db: Session = Depends(get_db)):
    #Calculate Bonus (Ratings and Perc Bonus: 5 - 25%, 4 - 20%, 3 - 10%)
    if emp.rating == 5:
        bonus = emp.base_salary * 0.25
    elif emp.rating == 4:
        bonus = emp.base_salary * 0.20
    elif emp.rating == 3:
        bonus = emp.base_salary * 0.10
    else:
        bonus = 0
    # Calculate total salary
    total_salary = emp.base_salary + bonus

    # Create new employee object (maps to DB table)
    new_employee = models.Employee(
        name=emp.name,                  #Converting Python Data into DB row
        department=emp.department,
        base_salary=emp.base_salary,
        rating=emp.rating,
        bonus=bonus,
        total_salary=total_salary
    )
    # Add employee to DB
    db.add(new_employee)

    # Commit changes (save to DB)
    db.commit()

    # Refresh object to get updated data (like auto-generated ID)
    db.refresh(new_employee)
    
    return new_employee     #return saved Employee

#GET API To create employee  -- READ Operation
@app.get("/employees")
def get_employees(db: Session = Depends(get_db)):
    return db.query(models.Employee).all()
# def create_emloyee(emp: Employee):  #add employee Function
#     return {
#         "message": "Employee received",
#         "data": emp
#     }



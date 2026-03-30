from pydantic import BaseModel
#This class is for request validation
#Validates incoming request
#Ensures correct data types
class EmployeeCreate(BaseModel):
    name: str
    department: str
    base_salary: float
    rating: int
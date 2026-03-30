# 🚀 Employee Performance & Salary Management System (Backend)

This is a backend API project built using **FastAPI** and **MySQL** to
manage employee performance and salary calculations.

## 🧰 Tech Stack

-   Python 3.x
-   FastAPI
-   Uvicorn
-   SQLAlchemy
-   MySQL
-   PyMySQL

## 📁 Project Structure

employee_system_api/
│ 
├── main.py 
├── database.py 
├── models.py 
├──schemas.py 
├── services.py 
├── venv/

## ⚙️ Setup Instructions

### 1. Clone Repository

git clone `<your-repo-url>`{=html} cd employee_system_api

### 2. Create Virtual Environment

python -m venv venv venv`\Scripts`{=tex}`\activate`{=tex}

### 3. Install Dependencies

pip install fastapi uvicorn sqlalchemy pymysql

### 4. Setup MySQL Database

CREATE DATABASE employee_system; USE employee_system;

CREATE TABLE employees ( id INT AUTO_INCREMENT PRIMARY KEY, name
VARCHAR(100), department VARCHAR(100), base_salary DECIMAL(10,2), rating
INT, bonus DECIMAL(10,2), total_salary DECIMAL(10,2), created_at
TIMESTAMP DEFAULT CURRENT_TIMESTAMP );

### 5. Configure Database

DATABASE_URL =
"mysql+pymysql://root:YOUR_PASSWORD@localhost/employee_system"

### 6. Run Application

uvicorn main:app --reload

## 🌐 Access API

http://127.0.0.1:8000/ http://127.0.0.1:8000/docs

## 👨‍💻 Author

Vivek Gummadishetty

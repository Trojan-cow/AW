# list employee
# retrieve employee by id/ name
from fastapi import FastAPI
from attendance_management import Employee, Register
from pydantic import BaseModel
from datetime import date

app = FastAPI()
emp_id = 100
emp1 = Employee("Rahul", emp_id, "MD", "Male", date(1992, 10, 20))
emp2 = Employee("Sonia", 101, "COO", "Female", date(1996, 10, 4))
reg = Register()
reg.add(emp1)
reg.add(emp2)


@app.get("/employee/")
def get_list():
    return reg.emp_list


@app.get("/empid/")
def read_item(employ_id: int):
    check = reg.read_by_id(employ_id)
    if check:
        return reg.read_by_id(employ_id)
    else:
        return {"code": 200, "Message": "ID does not exist in the register"}


class Employ(BaseModel):
    name: str
    emp_id: int
    designation: str
    gender: str
    dob: date


@app.post("/employee/")
async def create_employee(item: Employ):
    reg.add(item)
    return {"code": 200, "message": "employ added successfully"}


@app.put("/employee")
async def update_name(emp: Employ, employ_id: int):
    count = 0
    for employee in reg.emp_list:
        if employ_id == employee.emp_id:
            employee.name = emp.name
            employee.gender = emp.gender
            employee.designation = emp.designation
            employee.dob = emp.dob
            count += 1
            return {"code": 200, "Message": "Employee successfully updated"}
        else:
            return {"code": 200, "Message": "Employee ID doesn't exist"}


@app.delete("/employee")
async def delete_employee(employ_id: int):
    check = reg.read_by_id(employ_id)
    if check:
        reg.remove(employ_id)
        return {"code": 200, "message": "employee deleted successfully."}
    else:
        return {"code": 400, "message": "invalid employee ID"}

from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date
import mysql.connector


connection = mysql.connector.connect(host='localhost',
                                     database='aw_internship',
                                     user='root',
                                     password='Ampl1f1er@aw')
cursor = connection.cursor()

app = FastAPI()


def employee_list():
    register = cursor.fetchall()
    emp_list = []
    column_names = [column[0] for column in cursor.description]

    for employee in register:
        emp_list.append(dict(zip(column_names, employee)))
    return emp_list


def check(employ_id):
    cursor.execute(f"select * from employee where emp_id={employ_id};")
    x = employee_list()
    if x:
        return x
    else:
        return 0


@app.get("/employee/")
def get_list():
    cursor.execute("select * from employee;")
    x = employee_list()
    return x


@app.get("/empid/")
def read_item(employ_id: int):
    cursor.execute(f"select * from employee where emp_id={employ_id};")
    x = employee_list()
    if x:
        return x
    else:
        return {"code": 402, "message": "Invalid Employee ID"}


class Employ(BaseModel):
    name: str
    emp_id: int
    designation: str
    gender: str
    dob: date


@app.post("/employee/")
async def create_employee(emp: Employ):
    x = check(emp.emp_id)
    if not x:
        cursor.execute(f"insert into employee "
                       f"values('{emp.name}', {emp.emp_id}, '{emp.designation}', '{emp.dob}','{emp.gender}');")
        return {"code": 200, "Message": "Employee successfully added"}
    else:
        return {"code": 402, "message": "Employee ID exists already"}


@app.put("/employee")
async def update_name(emp: Employ, employ_id: int):
    x = check(employ_id)
    if x:
        cursor.execute(f"update employee "
                       f"set name = '{emp.name}', "
                       f"designation = '{emp.designation}', dob = '{emp.dob}', gender='{emp.gender}' "
                       f"where emp_id={employ_id};")
        return {"code": 200, "Message": "Employee successfully updated"}
    else:
        cursor.execute(f"insert into employee "
                       f"values('{emp.name}', {emp.emp_id}, '{emp.designation}', '{emp.dob}','{emp.gender}');")
        return {"code": 200, "Message": "Employee doesn't exist, New Employee Created"}


@app.delete("/employee")
async def delete_employee(employ_id: int):
    x = check(employ_id)
    if x:
        cursor.execute(f"delete from employee where emp_id={employ_id}")
        return {"code": 200, "message": "employee deleted successfully."}
    else:
        return {"code": 404, "Message": "Employee ID doesn't exist"}

# sealizers -schemas

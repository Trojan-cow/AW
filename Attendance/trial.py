# employee object
# add employee functionality
# remove employee by id
# login employee (time to be captured)
# logout
# print register in tabular form
from attendance_management import Employee, Register, Attendance
from datetime import datetime
import pandas as pd

emp_id = 100
emp1 = Employee("Rahul", emp_id, "MD", "Male", datetime.strptime("1986-07-15", "%Y-%m-%d"))
reg = Register()
reg.add(emp1)

while True:
    to_do = input("Enter \'add\' or \'delete\' else press any key and \'enter\' to enter the log:\n")
    if to_do == "add":
        num = int(input("Enter the number of Employees to be added:"))
        count = len(reg.emp_list)
        while count <= num:
            emp_id = int(input("enter id:"))
            name = input("Enter name:")
            designation = input("Enter Designation:")
            dob = datetime.strptime(input("DOB (yyyy-mm-dd):"), "%Y-%m-%d")
            gender = input("Enter Gender: ")

            emp = Employee(name, emp_id, designation, gender, dob)
            reg.add(emp)
            count += 1

    elif to_do == "delete":
        emp_id = int(input("Enter employee id:"))
        reg.remove(emp_id)

    else:
        break

num = int(input("enter the number of employees logging in or out:"))
count = 0
while count < num:
    user = int(input("enter your ID:"))
    log = Attendance()
    x = len(reg.emp_list)
    for employee in reg.emp_list:
        x -= 1
        if user == employee.emp_id:
            e_type = input("login or logout:")
            if e_type == "login":
                log.login(user)
                count += 1
            elif e_type == "logout":
                log.logout(user)
                count += 1
        elif x == 0 and user != employee.emp_id:
            print("invalid user, enter again")

x = []
y = []
n = 0
for Employee in reg.emp_list:
    z = Employee.__dict__
    x.append(z.values())
    n += 1
    y.append(n)
print(pd.DataFrame(x, y, z))

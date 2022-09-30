from datetime import date, datetime


class Employee:
    default_dob = date(1998, 5, 9)

    def __init__(self, name: str, emp_id: int, designation: str, gender: str, dob: date = None):
        self.name = name
        self.emp_id = emp_id
        self.designation = designation
        self.dob = dob
        self.gender = gender


class Register:
    def __init__(self):
        self.emp_list = []

    def get_list(self):
        return self.emp_list

    def add(self, employee):
        self.emp_list.append(employee)

    def read_by_id(self, emp_id):
        for employee in self.emp_list:
            if emp_id == employee.emp_id:
                return employee
        return None

    def remove(self, emp_id):
        employee = self.read_by_id(emp_id)
        if employee:
            self.emp_list.remove(employee)
            # or del employee


class Attendance:
    def __init__(self):
        self.att_in = []
        self.att_out = []

    def login(self, emp_id):
        now = datetime.now()
        login_time = now.strftime("%H:%M:%S")
        d = {emp_id: login_time}
        self.att_in.append(d)

    def logout(self, emp_id):
        now = datetime.now()
        logout_time = now.strftime("%H:%M:%S")
        d = {emp_id: logout_time}
        self.att_out.append(d)

        # for obj in self.att_out:
        #     print(obj[emp_id])

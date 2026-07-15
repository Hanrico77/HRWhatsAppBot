from repository.employee_repository import EmployeeRepository


class EmployeeService:

    def __init__(self):

        self.repository = EmployeeRepository()

    def get_employee(self, emp_no):

        return self.repository.get_employee(emp_no)
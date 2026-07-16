from commands.base_command import BaseCommand
from services.employee_service import EmployeeService


class EmployeeCommand(BaseCommand):

    def __init__(self):
        self.employee_service = EmployeeService()

    def execute(self, arguments):

        if len(arguments) == 0:
            return {"error": "Employee number missing"}

        return self.employee_service.get_employee(arguments[0])
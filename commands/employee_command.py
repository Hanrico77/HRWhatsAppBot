from commands.base_command import BaseCommand
from services.employee_service import EmployeeService
from formatters.employee_formatter import EmployeeFormatter


class EmployeeCommand(BaseCommand):

    def __init__(self):
        self.employee_service = EmployeeService()

    def execute(self, arguments):

        if len(arguments) == 0:
            return "❌ Employee number missing."

        employee = self.employee_service.get_employee(arguments[0])

        return EmployeeFormatter.format_employee(employee)
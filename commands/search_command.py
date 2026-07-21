from commands.base_command import BaseCommand
from services.employee_service import EmployeeService
from formatters.employee_formatter import EmployeeFormatter


class SearchCommand(BaseCommand):

    def __init__(self):
        self.employee_service = EmployeeService()

    def execute(self, arguments):

        if len(arguments) == 0:
            return "❌ Search text missing."

        search_text = " ".join(arguments)

        employees = self.employee_service.search_employee(search_text)

        return EmployeeFormatter.format_search(employees)
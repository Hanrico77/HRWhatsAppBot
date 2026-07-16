from commands.base_command import BaseCommand
from services.employee_service import EmployeeService


class SearchCommand(BaseCommand):

    def __init__(self):
        self.employee_service = EmployeeService()

    def execute(self, arguments):

        if len(arguments) == 0:
            return {"error": "Search text missing"}

        search_text = " ".join(arguments)

        return self.employee_service.search_employee(search_text)
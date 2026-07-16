from commands.employee_command import EmployeeCommand
from commands.search_command import SearchCommand


class CommandRegistry:

    def __init__(self):

        self.commands = {
            "employee": EmployeeCommand(),
            "search": SearchCommand()
        }

    def get(self, name):

        return self.commands.get(name.lower())
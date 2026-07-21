from commands.employee_command import EmployeeCommand
from commands.search_command import SearchCommand
from commands.leave_command import LeaveCommand

class CommandRegistry:

    def __init__(self):

        self.commands = {
            "employee": EmployeeCommand(),
            "search": SearchCommand(),
            "leave": LeaveCommand()
        }

    def get(self, name):

        return self.commands.get(name.lower())
from commands.employee_command import EmployeeCommand
from commands.search_command import SearchCommand
from commands.leave_command import LeaveCommand
from commands.help_command import HelpCommand
from commands.manager_command import ManagerCommand
from commands.profile_command import ProfileCommand
from commands.reports_command import ReportsCommand

class CommandRegistry:

    def __init__(self):

        self.commands = {
            "employee": EmployeeCommand(),
            "search": SearchCommand(),
            "leave": LeaveCommand(),
            "help": HelpCommand(),
            "manager": ManagerCommand(),
            "profile": ProfileCommand(),
            "reports": ReportsCommand()
        }

    def get(self, name):

        return self.commands.get(name.lower())
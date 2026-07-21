from commands.base_command import BaseCommand
from services.leave_service import LeaveService
from formatters.leave_formatter import LeaveFormatter


class LeaveCommand(BaseCommand):

    def __init__(self):
        self.service = LeaveService()

    def execute(self, arguments):

        if len(arguments) == 0:
            return "❌ Employee number missing."

        rows = self.service.get_leave(arguments[0])

        return LeaveFormatter.format_leave(rows)
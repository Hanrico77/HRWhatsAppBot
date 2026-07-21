from commands.base_command import BaseCommand
from services.reports_service import ReportsService


class ReportsCommand(BaseCommand):

    def __init__(self):

        self.service = ReportsService()

    def execute(self, arguments):

        if len(arguments) == 0:
            return "Usage:\nreports 0012345"

        return self.service.get_reports(arguments[0])
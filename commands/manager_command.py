from commands.base_command import BaseCommand
from services.manager_service import ManagerService


class ManagerCommand(BaseCommand):

    def __init__(self):

        self.service = ManagerService()

    def execute(self, arguments):

        if len(arguments) == 0:
            return "Usage:\nmanager 0029424"

        return self.service.get_manager(arguments[0])
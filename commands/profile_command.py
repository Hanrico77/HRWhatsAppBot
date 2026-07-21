from commands.base_command import BaseCommand
from services.profile_service import ProfileService


class ProfileCommand(BaseCommand):

    def __init__(self):

        self.service = ProfileService()

    def execute(self, arguments):

        if len(arguments) == 0:
            return "Usage:\nprofile 0029424"

        return self.service.get_profile(arguments[0])
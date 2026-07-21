from commands.base_command import BaseCommand
from formatters.base_formatter import BaseFormatter


class HelpCommand(BaseCommand):

    def execute(self, arguments):

        message = BaseFormatter.title(
            "🤖",
            "HR Assistant"
        )

        message += (
            "Available Commands\n\n"

            "👤 employee 29424\n"
            "View employee details\n\n"

            "🔍 search hanrico\n"
            "Search for employees\n\n"

            "🌴 leave 29424\n"
            "View leave balances\n\n"

            "👔 manager 0029424\n"
            "View direct manager\n\n"

            "👤 profile 0029424\n"
            "Complete employee profile\n\n"

            "👥 reports 0029424\n"
            "View direct reports\n\n"

            "❓ help\n"
            "Show this help screen\n"
        )

        message += BaseFormatter.footer()

        return message
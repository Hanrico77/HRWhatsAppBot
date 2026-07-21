from services.command_registry import CommandRegistry
from formatters.base_formatter import BaseFormatter


class CommandService:

    def __init__(self):
        self.registry = CommandRegistry()

    def execute(self, command: str):

        command = command.strip()

        if not command:
            return BaseFormatter.error("Empty command.")

        parts = command.split()

        action = parts[0].lower()
        arguments = parts[1:]

        # Welcome commands
        if action in [
            "hi",
            "hello",
            "hey",
            "start"
        ]:
            return BaseFormatter.welcome()

        # Find the command handler
        handler = self.registry.get(action)

        if handler is None:
            return BaseFormatter.error(
                "Unknown command.\n\n"
                "Type 'help' to see available commands."
            )

        # Execute the command
        return handler.execute(arguments)
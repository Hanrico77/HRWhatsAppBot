from services.command_registry import CommandRegistry


class CommandService:

    def __init__(self):
        self.registry = CommandRegistry()

    def execute(self, command: str):

        command = command.strip()

        if not command:
            return {"error": "Empty command"}

        parts = command.split()

        action = parts[0]

        arguments = parts[1:]

        handler = self.registry.get(action)

        if handler is None:
            return {
                "error": f"Unknown command '{action}'"
            }

        return handler.execute(arguments)
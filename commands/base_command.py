class BaseCommand:

    def execute(self, arguments):
        raise NotImplementedError("Command must implement execute()")
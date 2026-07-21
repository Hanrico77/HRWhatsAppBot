class BaseFormatter:

    LINE = "════════════════════════"

    @staticmethod
    def title(icon, title):

        return (
            f"{BaseFormatter.LINE}\n"
            f"{icon} {title.upper()}\n"
            f"{BaseFormatter.LINE}\n\n"
        )

    @staticmethod
    def footer():

        return (
            "\n"
            "────────────────────────\n"
            "🤖 HR Assistant v1.0\n"
            "© 2026 PathCare HR AI"
        )

    @staticmethod
    def welcome(name=""):

        message = BaseFormatter.title(
            "👋",
            "Welcome"
        )

        if name:
            message += f"Hello {name}!\n\n"

        message += (
            "I'm your HR Assistant.\n\n"
            "I can help you with:\n\n"
            "👤 employee 0029424\n"
            "🔍 search hanrico\n"
            "🌴 leave 0029424\n"
            "❓ help\n"
        )

        message += BaseFormatter.footer()

        return message

    @staticmethod
    def error(message):

        return (
            BaseFormatter.title(
                "❌",
                "Error"
            )
            + message
            + BaseFormatter.footer()
        )

    @staticmethod
    def success(message):

        return (
            BaseFormatter.title(
                "✅",
                "Success"
            )
            + message
            + BaseFormatter.footer()
        )
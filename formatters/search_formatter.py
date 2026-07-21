from formatters.base_formatter import BaseFormatter


class SearchFormatter:

    @staticmethod
    def format_search(rows):

        if len(rows) == 0:
            return BaseFormatter.error(
                "No employees found."
            )

        message = BaseFormatter.title(
            "🔍",
            "Search Results"
        )

        message += f"Found {len(rows)} employee(s)\n\n"

        for i, row in enumerate(rows, start=1):

            message += (
                f"{i}. {row['name']} {row['surname']}\n"
                f"🆔 {row['emp_no']}\n"
                f"💼 {row['job_title']}\n"
            )

            if i < len(rows):
                message += "\n────────────────────────\n\n"

        message += BaseFormatter.footer()

        return message
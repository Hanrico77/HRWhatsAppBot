from formatters.base_formatter import BaseFormatter


class LeaveFormatter:

    @staticmethod
    def format_leave(rows):

        if len(rows) == 0:
            return BaseFormatter.error(
                "No leave information found."
            )

        emp_no = rows[0]["emp_no"]
        employee = rows[0]["employee_name"]

        message = BaseFormatter.title(
            "🌴",
            "Leave Balances"
        )

        message += f"👤 {employee}\n\n"
        message += f"🆔 {emp_no}\n\n"

        icons = {
            "Annual Leave": "🌴",
            "Study Leave": "📚",
            "Family Responsibility Leave": "👨‍👩‍👧"
        }

        for row in rows:

            icon = icons.get(row["leave_type"], "•")

            message += (
                f"{icon} {row['leave_type']}\n"
                f"{row['balance']} days\n\n"
            )

        message += BaseFormatter.footer()

        return message
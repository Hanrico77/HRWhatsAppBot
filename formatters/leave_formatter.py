class LeaveFormatter:

    @staticmethod
    def format_leave(rows):

        if len(rows) == 0:
            return "❌ Employee not found or no leave balances."

        emp_no = rows[0]["emp_no"]
        employee_name = rows[0]["employee_name"]

        message = "🌴 Leave Balances\n\n"
        message += f"👤 {employee_name}\n"
        message += f"🆔 Employee #: {emp_no}\n\n"

        for row in rows:
            message += (
                f"• {row['leave_type']}: {row['balance']} days\n"
            )

        return message
from formatters.base_formatter import BaseFormatter


class EmployeeFormatter:

    @staticmethod
    def format_employee(employee):

        if employee is None:

            return BaseFormatter.error(
                "Employee not found."
            )

        message = BaseFormatter.title(
            "👤",
            "Employee Details"
        )

        message += f"👤 {employee['name']} {employee['surname']}\n\n"

        message += f"🆔 Employee\n{employee['emp_no']}\n\n"

        message += f"💼 Job Title\n{employee['job_title']}\n\n"

        message += f"🏢 Department\n{employee['department']}\n\n"

        message += f"📧 Email\n{employee['email']}"

        message += BaseFormatter.footer()

        return message
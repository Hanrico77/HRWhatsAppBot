from formatters.base_formatter import BaseFormatter


class ManagerFormatter:

    @staticmethod
    def format(manager):

        message = BaseFormatter.title(
            "👔",
            "Manager"
        )

        message += (
            f"Employee\n"
            f"{manager['employee_name']} {manager['employee_surname']}\n\n"

            f"Manager\n"
            f"{manager['manager_name']}\n\n"

            f"Employee No\n"
            f"{manager['manager_emp_no']}\n\n"

            f"Email\n"
            f"{manager['manager_email']}\n"
        )
        message += BaseFormatter.quick_actions([
            f"👤 profile {manager['emp_no'].strip()}",
            f"🌴 leave {manager['emp_no'].strip()}",
            f"👥 reports {manager['emp_no'].strip()}"
        ])
        message += BaseFormatter.footer()

        return message

    @staticmethod
    def not_found(emp_no):

        return BaseFormatter.error(
            f"No manager found for employee {emp_no}"
        )
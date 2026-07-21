from formatters.base_formatter import BaseFormatter


class ProfileFormatter:

    @staticmethod
    def format(employee, leave, manager):

        leave_text = ""

        for item in leave:

            balance = float(item["balance"])

            if balance.is_integer():
                balance = int(balance)

            leave_text += (
                f"• {item['leave_type']}: {balance} day(s)\n"
            )

        message = BaseFormatter.title(
            "👤",
            "Employee Profile"
        )

        message += (
            "📋 EMPLOYEE\n"
            "────────────────────────\n"

            f"Name\n"
            f"{employee['name']} {employee['surname']}\n\n"

            f"Employee No\n"
            f"{employee['emp_no'].strip()}\n\n"

            f"Job Title\n"
            f"{employee['job_title']}\n\n"

            "🏢 ORGANISATION\n"
            "────────────────────────\n"

            f"Department\n"
            f"{employee['department']}\n\n"

            f"Manager\n"
            f"{manager['manager_name']}\n\n"

            "🌴 LEAVE BALANCES\n"
            "────────────────────────\n"

            f"{leave_text}\n"

            "📧 CONTACT\n"
            "────────────────────────\n"

            f"{employee['email']}\n"
        )
        message += BaseFormatter.quick_actions([
            f"👔 manager {employee['emp_no'].strip()}",
            f"👥 reports {employee['emp_no'].strip()}",
            f"🌴 leave {employee['emp_no'].strip()}",
            f"🔍 search {employee['surname']}"
        ])
        
        message += BaseFormatter.footer()

        return message

    @staticmethod
    def not_found(emp_no):

        return BaseFormatter.error(
            f"Employee {emp_no} not found."
        )
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
    
    @staticmethod    
    def format_search(employees):

        if len(employees) == 0:

            return BaseFormatter.error(
                "No employees found."
            )

        message = BaseFormatter.title(
            "🔍",
            "Search Results"
        )

        message += (
            f"Found {len(employees)} employee(s)\n\n"
        )

        actions = []

        for index, employee in enumerate(employees, start=1):

            emp_no = employee["emp_no"].strip()

            message += (
                f"{index}. {employee['name']} {employee['surname']}\n"
                f"   #{emp_no}\n"
                f"   💼 {employee['job_title']}\n\n"
            )

            # Only generate quick actions for the first 5 employees
            if index <= 5:
                actions.append(f"👤 profile {emp_no}")
                actions.append(f"🌴 leave {emp_no}")
                actions.append(f"👔 manager {emp_no}")

        message += BaseFormatter.quick_actions(actions)
        message += BaseFormatter.footer()

        return message
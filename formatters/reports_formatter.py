from formatters.base_formatter import BaseFormatter


class ReportsFormatter:

    @staticmethod
    def format(manager_emp_no, employees):

        message = BaseFormatter.title(
            "👥",
            "Direct Reports"
        )

        if len(employees) == 0:

            message += (
                "No direct reports found.\n"
            )

        else:

            message += (
                f"Employees ({len(employees)})\n\n"
            )

            for index, employee in enumerate(employees, start=1):

                message += (
                    f"{index}. {employee['name']} {employee['surname']}\n"
                    f"   {employee['job_title']}\n"
                    f"   #{employee['emp_no']}\n\n"
                )

            message += "\n"

            actions = []
           

            for employee in employees[:5]:

                emp_no = employee["emp_no"].strip()

                actions.append(f"👤 profile {emp_no}")
                actions.append(f"🌴 leave {emp_no}")


            message += BaseFormatter.quick_actions(actions)

        message += BaseFormatter.footer()

        return message
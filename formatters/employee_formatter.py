class EmployeeFormatter:

    @staticmethod
    def format_employee(employee):

        if employee is None:
            return "❌ Employee not found."

        return (
            "👤 Employee Details\n\n"
            f"Name       : {employee['name']} {employee['surname']}\n"
            f"Employee # : {employee['emp_no']}\n"
            f"Job Title  : {employee['job_title']}\n"
            f"Department : {employee['department']}\n"
            f"Email      : {employee['email']}"
        )

    @staticmethod
    def format_search(results):

        if not results:
            return "❌ No employees found."

        response = f"🔍 Found {len(results)} employee(s)\n\n"

        for i, employee in enumerate(results, start=1):
            response += (
                f"{i}. {employee['name']} {employee['surname']}\n"
                f"   #{employee['emp_no']}\n"
                f"   {employee['job_title']}\n"
                f"   {employee['department']}\n\n"
            )

        return response
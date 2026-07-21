from services.employee_service import EmployeeService
from services.leave_service import LeaveService
from services.manager_service import ManagerService
from formatters.profile_formatter import ProfileFormatter


class ProfileService:

    def __init__(self):

        self.employee_service = EmployeeService()
        self.leave_service = LeaveService()
        self.manager_service = ManagerService()

    def get_profile(self, emp_no):

        employee = self.employee_service.repository.get_employee(emp_no)

        if employee is None:
            return ProfileFormatter.not_found(emp_no)

        leave = self.leave_service.repository.get_leave_balances(emp_no)

        manager = self.manager_service.repository.get_manager(emp_no)

        return ProfileFormatter.format(
            employee,
            leave,
            manager
        )
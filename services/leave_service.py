from repository.leave_repository import LeaveRepository


class LeaveService:

    def __init__(self):
        self.repository = LeaveRepository()

    def get_leave(self, emp_no):
        return self.repository.get_leave_balances(emp_no)
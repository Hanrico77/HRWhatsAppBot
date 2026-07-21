from repository.manager_repository import ManagerRepository
from formatters.manager_formatter import ManagerFormatter


class ManagerService:

    def __init__(self):

        self.repository = ManagerRepository()

    def get_manager(self, emp_no):

        manager = self.repository.get_manager(emp_no)

        if manager is None:
            return ManagerFormatter.not_found(emp_no)

        return ManagerFormatter.format(manager)
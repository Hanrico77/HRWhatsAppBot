from repository.reports_repository import ReportsRepository
from formatters.reports_formatter import ReportsFormatter


class ReportsService:

    def __init__(self):

        self.repository = ReportsRepository()

    def get_reports(self, manager_emp_no):

        employees = self.repository.get_reports(manager_emp_no)

        return ReportsFormatter.format(
            manager_emp_no,
            employees
        )
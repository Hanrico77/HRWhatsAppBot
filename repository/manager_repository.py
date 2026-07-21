from database.sql import Database


class ManagerRepository:

    def get_manager(self, emp_no):

        sql = """
        SELECT

            [Emp No]           AS emp_no,
            Name               AS employee_name,
            Surname            AS employee_surname,

            [Manager Name]     AS manager_name,
            [Manager Emp No]   AS manager_emp_no,
            [Manager Email]    AS manager_email

        FROM vw_auditHR

        WHERE [Emp No] = ?
        """

        rows = Database.execute_query(sql, (emp_no,))

        if len(rows) == 0:
            return None

        return rows[0]
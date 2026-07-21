from database.sql import Database


class ReportsRepository:

    def get_reports(self, manager_emp_no):

        sql = """
        SELECT

            RTRIM([Emp No])      AS emp_no,
            Name                 AS name,
            Surname              AS surname,
            Job_Title            AS job_title,
            Department           AS department

        FROM vw_auditHR

        WHERE RTRIM([Manager Emp No]) = ?

        ORDER BY
            Surname,
            Name
        """

        return Database.execute_query(
            sql,
            (manager_emp_no,)
        )
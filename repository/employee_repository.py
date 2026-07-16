from database.sql import Database


class EmployeeRepository:

    def get_employee(self, emp_no):

        sql = """

        SELECT
            [emp no]      AS emp_no,
            Name          AS name,
            Surname       AS surname,
            Job_Title     AS job_title,
            Department    AS department,
            Email         AS email

        FROM vw_auditHR

        WHERE [emp no] = ?

        """

        rows = Database.execute_query(sql, (emp_no,))

        if len(rows) == 0:
            return None

        return rows[0]


    def search_employee(self, search_text):

        sql = """
        SELECT TOP (20)

            [emp no]  AS emp_no,
            Name      AS name,
            Surname   AS surname,
            Job_Title AS job_title,
            Department AS department,
            Email     AS email

        FROM vw_auditHR

        WHERE
            Name LIKE ?
            OR Surname LIKE ? OR CAST([emp no] AS VARCHAR(20)) LIKE ?

        ORDER BY
            Surname,
            Name
        """

        search = f"%{search_text}%"

        return Database.execute_query(
            sql,
            (search, search, search)
        )
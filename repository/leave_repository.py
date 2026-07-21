from database.sql import Database


class LeaveRepository:

    def get_leave_balances(self, emp_no):

        sql = """
SELECT
    RTRIM(e.[emp no]) AS emp_no,
    RTRIM(e.Name) + ' ' + RTRIM(e.Surname) AS employee_name,
    CASE l.Lv_Type_Id
        WHEN '1' THEN 'Annual Leave'
        WHEN '2' THEN 'Study Leave'
        WHEN '5' THEN 'Family Responsibility Leave'
    END AS leave_type,
    l.Bal_Now AS balance
FROM Lv_Emp l
INNER JOIN vw_auditHR e
    ON RTRIM(e.[emp no]) = RTRIM(l.Emp_No)
WHERE l.Lv_Type_Id IN ('1','2','5')
  AND RTRIM(l.Emp_No) = ?
ORDER BY l.Lv_Type_Id
        """

        return Database.execute_query(
            sql,
            (emp_no,)
        )
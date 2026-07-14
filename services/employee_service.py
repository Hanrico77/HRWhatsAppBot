from database.sql import Database

db = Database()


class EmployeeService:

    def get_sql_version(self):

        rows = db.execute("SELECT @@VERSION")

        return rows[0][0]
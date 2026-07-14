import pyodbc
import config


class Database:

    def __init__(self):

        self.connection_string = (
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={config.SQL_SERVER};"
            f"DATABASE={config.SQL_DATABASE};"
            f"UID={config.SQL_USER};"
            f"PWD={config.SQL_PASSWORD};"
            "TrustServerCertificate=yes;"
        )

    def get_connection(self):

        return pyodbc.connect(self.connection_string)

    def execute(self, sql, params=None):

        conn = self.get_connection()

        cursor = conn.cursor()

        if params:
            cursor.execute(sql, params)
        else:
            cursor.execute(sql)

        rows = cursor.fetchall()

        conn.close()

        return rows
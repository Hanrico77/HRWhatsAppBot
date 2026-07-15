import pyodbc
import config


class Database:

    @staticmethod
    def get_connection():

    	return pyodbc.connect(

      		f"DRIVER={{{config.SQL_DRIVER}}};"
  	    	f"SERVER={config.SQL_SERVER};"
      		f"DATABASE={config.SQL_DATABASE};"
      		f"UID={config.SQL_USER};"
      		f"PWD={config.SQL_PASSWORD};"
      		"TrustServerCertificate=yes;"
    	)

    @staticmethod
    def execute_query(query, params=None):

        conn = Database.get_connection()

        cursor = conn.cursor()

        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        columns = [column[0] for column in cursor.description]

        rows = cursor.fetchall()

        result = []

        for row in rows:
            result.append(dict(zip(columns, row)))

        conn.close()

        return result
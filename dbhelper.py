import dbconfig
import psycopg2


class DBHelper():
    """docstring for DBHelper."""

    def connect(self, database="crimemap"):
        return psycopg2.connect(host='91.189.34.102', dbname=database, user=dbconfig.db_user, password=dbconfig.db_password)

    def get_all_inputs(self):
        connection = self.connect()
        try:
            query = "SELECT description FROM crimes;"
            with connection.cursor() as cursor:
                cursor.execute(query)
            return cursor.fetchall()
        finally:
            connection.close()

    def add_input(data):
        connection = self.connect()
        try:
            query = "INSERT INTO crimes (description) VALUES ('{}');".format(data)
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
        finally:
            connection.close()

    def clear_all(self):
        connection = self.connect()
        try:
            query = "DELETE FROM crimes;"
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
        finally:
            connection.close()

import dbconfig
import psycopg2


class DBHelper():
    """docstring for DBHelper."""

    def connect(self, database="crimemap"):
        return psycopg2.connect(host='localhost',
                                dbname=database, user=dbconfig.db_user,
                                password=dbconfig.db_password)

    def get_all_inputs(self):
        connection = self.connect()
        try:
            query = "SELECT description FROM crimes;"
            with connection.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall()
        except Exception as e:
            print(e)

    def add_input(self, data):
        connection = self.connect()
        query = "INSERT INTO crimes (description) VALUES ("+data+");"
        with connection.cursor() as cursor:
            cursor.execute(query)
        connection.close()

    def clear_all(self):
        connection = self.connect()
        try:
            query = "DELETE FROM crimes;"
            with connection.cursor() as cursor:
                cursor.execute(query)
        except Exception as e:
            print(e)

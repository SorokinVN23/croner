import sqlite3

class DataBase():
    def __init__(self, settings):
        self.settings = settings 
        
    def execute_query(self, query, params = None):
        connection = sqlite3.connect(self.settings.database, self.settings.timeout)

        try:
            cursor = connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            connection.commit()

            rows = cursor.fetchall()
            return rows
        
        except sqlite3.Error as e:
            connection.rollback()
            raise

        finally:
            connection.close()
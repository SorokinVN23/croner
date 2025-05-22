import sqlite3
import glob
import os
import re
from typing import Tuple

import core.store as cstore


class DataBase(cstore.Store):
    def __init__(self, settings):
        self.settings = settings
        self._init_database()
        self._apply_migrations() 

    def record_save(self, text):
        query = r"insert into records (text) values (?)"
        self.execute_query(query, (text,))

    def get_record_dates(self, limit : int = 30) -> Tuple:
        query = f"""SELECT DISTINCT DATE(time) AS date_only
            FROM Records
            ORDER BY date_only DESC
            limit {limit};"""
        rows = self.execute_query(query)
        res = tuple(row[0] for row in rows)
        return res

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

    def _init_database(self):
        query = f"""create table if not exists Migrations (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            applied_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );"""
        self.execute_query(query)

    def _apply_migrations(self):
        pattern = os.path.join(self.settings.migrations, "*.sql")
        paths = glob.glob(pattern)
        mykey = lambda path : int(re.search(r"(\d+)", path).group(0))
        paths.sort(key = mykey)

        query = "select name from Migrations"
        applyed_migrations = self.execute_query(query)
        applyed_migrations = {row[0] for row in applyed_migrations}

        insert_query = "INSERT INTO Migrations (name) VALUES (?)"

        for path in paths:
            migrate_name = os.path.basename(path)
            if migrate_name not in applyed_migrations:
                with open(path, "r") as f:
                    query = f.read()
                    self.execute_query(query)
                    self.execute_query(insert_query, (migrate_name,))
                    
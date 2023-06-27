import sqlite3


class _Database:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None

        self._connect()

    def _connect(self):
        self.conn = sqlite3.connect(self.db_file)

    def _disconnect(self):
        if self.conn:
            self.conn.close()

    def create_table(self, table_name, columns):
        with self.conn:
            cursor = self.conn.cursor()
            column_defs = ", ".join(columns)
            query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_defs})"
            cursor.execute(query)

    def insert_data(self, table_name, keys, values):
        with self.conn:
            cursor = self.conn.cursor()
            placeholders = ", ".join(["?"] * len(values))
            key_placeholders = ", ".join(keys)

            query = (
                f"INSERT INTO {table_name} ({key_placeholders}) VALUES ({placeholders})"
            )
            cursor.execute(query, values)

    def execute_query(self, query, params=None):
        with self.conn:
            cursor = self.conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor.fetchall()


# Singleton
db = _Database("main.db")

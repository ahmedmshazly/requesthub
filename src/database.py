import sqlite3

class Database:
    def __init__(self):
        try:
            self.conn = sqlite3.connect('database.db')
            self.cursor = self.conn.cursor()
        except Exception as e:
            return [1, str(e)]

    def execute_query(self, query, params=None):
        try:
            if params is None:
                self.cursor.execute(query)
            else:
                self.cursor.execute(query, params)
            self.conn.commit()
            return [0]
        except Exception as e:
            return [1, str(e)]

    def fetch_data(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            return [0, self.cursor.fetchall()]
        except Exception as e:
            return [1, str(e)]

    def close_connection(self):
        try:
            self.cursor.close()
            self.conn.close()
            return [0]
        except Exception as e:
            return [1, str(e)]

    def create_tables(self):
        create_users_table = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT,
            username TEXT UNIQUE,
            email TEXT UNIQUE,
            password TEXT,
            user_type TEXT
        )
        """
        return self.execute_query(create_users_table)

    def table_exists(self, table_name):
        try:
            query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';"
            self.cursor.execute(query)
            return [0, self.cursor.fetchone() is not None]
        except Exception as e:
            return [1, str(e)]

    def print_table_contents(self, table_name):
        try:
            if self.table_exists(table_name)[1]:
                query = f"SELECT * FROM {table_name};"
                self.cursor.execute(query)
                rows = self.cursor.fetchall()
                print(f"Contents of {table_name}:")
                for row in rows:
                    print(row)
                return [0]
            else:
                return [1, f"The table {table_name} does not exist."]
        except Exception as e:
            return [1, str(e)]

if __name__ == '__main__':
    db = Database()
    create_result = db.create_tables()

    if create_result[0] == 0:
        print("Tables created successfully.")
    else:
        print(f"Error creating tables: {create_result[1]}")

    table_exists_result = db.table_exists('users')

    if table_exists_result[0] == 0:
        if table_exists_result[1]:
            print("The 'users' table exists.")
            print_result = db.print_table_contents('users')
            if print_result[0] != 0:
                print(f"Error printing table contents: {print_result[1]}")
        else:
            print("The 'users' table does not exist.")
    else:
        print(f"Error checking table existence: {table_exists_result[1]}")

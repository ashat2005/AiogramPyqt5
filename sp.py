import sqlite3

class DataBaseCustomers:
    def __init__(self):
        self.connect = sqlite3.connect('customers.db')

    def connect_db(self):
        cursor = self.connect.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS customers (
        first_name VARCHAR(255),
        last_name VARCHAR(255),
        username VARCHAR(255),
        user_id INTEGER,
        phone_number INTEGER DEFAULT 0
        );""")
        self.connect.commit()

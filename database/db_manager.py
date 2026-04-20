"""
School Health Hub (SHH)
This is the flexible database manager which handles connections, queries and CRUD methods.
Author: Ifende Daniel
"""

import sqlite3


class DatabaseManager:
    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self._initialize_db()

    def _initialize_db(self):
        with open("database/schema.sql") as f:
            instruction = f.read()

        self.cursor.executescript(instruction)

    def create_user(
        self,
        username,
        password_hash,
        user_type,
        first_name,
        last_name,
        phone,
    ):

        self.cursor.execute(
            "INSERT INTO users (username, password_hash, user_type, first_name, last_name, phone) VALUES (?, ?, ?, ?, ?, ?)",
            (
                username,
                password_hash,
                user_type,
                first_name,
                last_name,
                phone,
            ),
        )

        self.connection.commit()

    def get_user_by_username(self, username):
        self.cursor.execute(
            "SELECT * FROM users WHERE username = ?", (username,)
        )
        return self.cursor.fetchone()

    def get_all_users(self):
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()

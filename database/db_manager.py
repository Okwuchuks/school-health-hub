"""
School Health Hub (SHH)
This is the flexible database manager which handles connections, queries and CRUD methods.
Author: Ifende Daniel
"""

import sqlite3


class DatabaseManager:
    def __init__(self, db_path, encyrpter):
        self.connection = sqlite3.connect(db_path)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
        self.encyrpter = encyrpter
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
        self.cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        return self.cursor.fetchone()

    def get_all_users(self):
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()

    def _map_student_row(self, row):
        """Private helper to transform a single encrypted SQLite Row into a plaintext dict."""
        student_data = {}

        student_data["student_id"] = row["student_id"]
        student_data["enrollment_year"] = row["enrollment_year"]
        student_data["blood_group"] = row["blood_group"]
        student_data["gender"] = row["gender"]
        student_data["hostel"] = row["hostel"]
        student_data["is_active"] = row["is_active"]

        student_data["first_name"] = self.encyrpter.decrypt(row["first_name"])
        student_data["middle_name"] = self.encyrpter.decrypt(row["middle_name"]) if row["middle_name"] else ""
        student_data["last_name"] = self.encyrpter.decrypt(row["last_name"])
        student_data["date_of_birth"] = self.encyrpter.decrypt(row["date_of_birth"])
        student_data["emergency_contact_name"] = self.encyrpter.decrypt(row["emergency_contact_name"])
        student_data["emergency_no"] = self.encyrpter.decrypt(row["emergency_no"])

        return student_data

    def create_student(
        self,
        first_name,
        middle_name,
        last_name,
        date_of_birth,
        enrollment_year,
        blood_group,
        gender,
        hostel,
        emergency_contact_name,
        emergency_no,
    ):

        enc_first_name = self.encyrpter.encrypt(first_name)
        enc_middle_name = self.encyrpter.encrypt(middle_name) if middle_name else ""
        enc_last_name = self.encyrpter.encrypt(last_name)
        enc_dob = self.encyrpter.encrypt(date_of_birth)
        enc_emergency_name = self.encyrpter.encrypt(emergency_contact_name)
        enc_emergency_no = self.encyrpter.encrypt(emergency_no)

        self.cursor.execute(
            "INSERT INTO students (first_name, middle_name, last_name, date_of_birth, enrollment_year, blood_group, gender, hostel, emergency_contact_name, emergency_no) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                enc_first_name,
                enc_middle_name,
                enc_last_name,
                enc_dob,
                enrollment_year,
                blood_group,
                gender,
                hostel,
                enc_emergency_name,
                enc_emergency_no,
            ),
        )
        self.connection.commit()

    def get_all_students(self):
        self.cursor.execute(
            "SELECT * FROM students",
        )
        return [self._map_student_row(row) for row in self.cursor.fetchall()]

    def get_student_by_name(self, student_name):

        enc_student_name = self.encyrpter.encrypt(student_name)

        self.cursor.execute("SELECT * FROM students WHERE first_name = ?", (enc_student_name,))

        return [self._map_student_row(row) for row in self.cursor.fetchall()]

    def delete_student(self, student_id):
        self.cursor.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
        self.connection.commit()

    def _map_staff_row(self, row):
        """Private helper to transform a single encrypted SQLite Row into a plaintext dict."""

        staff_data = {}

        staff_data["staff_id"] = row["staff_id"]
        staff_data["join_year"] = row["join_year"]
        staff_data["blood_group"] = row["blood_group"]
        staff_data["gender"] = row["gender"]
        staff_data["staff_office"] = row["staff_office"]
        staff_data["is_active"] = row["is_active"]
        staff_data["role"] = row["role"]

        staff_data["first_name"] = self.encyrpter.decrypt(row["first_name"])
        staff_data["middle_name"] = self.encyrpter.decrypt(row["middle_name"]) if row["middle_name"] else ""
        staff_data["last_name"] = self.encyrpter.decrypt(row["last_name"])
        staff_data["date_of_birth"] = self.encyrpter.decrypt(row["date_of_birth"])
        staff_data["emergency_contact_name"] = self.encyrpter.decrypt(row["emergency_contact_name"])
        staff_data["emergency_no"] = self.encyrpter.decrypt(row["emergency_no"])

        return staff_data

    def create_staff(
        self,
        first_name,
        middle_name,
        last_name,
        date_of_birth,
        join_year,
        blood_group,
        gender,
        staff_office,
        emergency_contact_name,
        emergency_no,
        role,
    ):

        enc_first_name = self.encyrpter.encrypt(first_name)
        enc_middle_name = self.encyrpter.encrypt(middle_name) if middle_name else ""
        enc_last_name = self.encyrpter.encrypt(last_name)
        enc_dob = self.encyrpter.encrypt(date_of_birth)
        enc_emergency_name = self.encyrpter.encrypt(emergency_contact_name)
        enc_emergency_no = self.encyrpter.encrypt(emergency_no)

        self.cursor.execute(
            "INSERT INTO staff (first_name, middle_name, last_name, date_of_birth, join_year, blood_group, gender, staff_office, emergency_contact_name, emergency_no, role) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                enc_first_name,
                enc_middle_name,
                enc_last_name,
                enc_dob,
                join_year,
                blood_group,
                gender,
                staff_office,
                enc_emergency_name,
                enc_emergency_no,
                role,
            ),
        )
        self.connection.commit()

    def get_all_staff(self):
        self.cursor.execute(
            "SELECT * FROM staff",
        )
        return [self._map_staff_row(row) for row in self.cursor.fetchall()]

    def _map_visit_row(self, row):
        """Private helper to transform a single encrypted SQLite Row into a plaintext dict."""

        visits_data = {}

        visits_data["visit_id"] = row["visit_id"]
        visits_data["patient_type"] = row["patient_type"]
        visits_data["patient_id"] = row["patient_id"]
        visits_data["user_id"] = row["user_id"]
        visits_data["term"] = row["term"]
        visits_data["symptom_category"] = row["symptom_category"]
        visits_data["visit_datetime"] = row["visit_datetime"]

        visits_data["complaint"] = self.encyrpter.decrypt(row["complaint"])
        visits_data["action_taken"] = self.encyrpter.decrypt(row["action_taken"])

        return visits_data

    def add_visit(self, patient_type, patient_id, user_id, term, complaint, symptom_category, action_taken):

        enc_complaint = self.encyrpter.encrypt(complaint)
        enc_action_taken = self.encyrpter.encrypt(action_taken)

        self.cursor.execute(
            "INSERT into visits (patient_type, patient_id, user_id, term, complaint, symptom_category, action_taken) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (patient_type, patient_id, user_id, term, enc_complaint, symptom_category, enc_action_taken),
        )
        self.connection.commit()

    def get_all_visits(self):
        self.cursor.execute(
            "SELECT * FROM visits",
        )
        return [self._map_visit_row(row) for row in self.cursor.fetchall()]

    def get_visits_by_patient(self, patient_id, patient_type):
        """Fetches and decrypts medical history for a specific student or staff member."""
        self.cursor.execute(
            "SELECT * FROM visits WHERE patient_id = ? AND patient_type = ? ORDER BY visit_datetime DESC",
            (patient_id, patient_type),
        )
        return [self._map_visit_row(row) for row in self.cursor.fetchall()]

    def add_staff_role(self, role_name):
        self.cursor.execute("INSERT OR IGNORE INTO staff_roles (role_name) VALUES (?)", (role_name,))
        self.connection.commit()

    def get_all_roles(self):
        self.cursor.execute("SELECT role_name FROM staff_roles")
        return [row["role_name"] for row in self.cursor.fetchall()]

    def add_staff_office(self, office_name):
        self.cursor.execute("INSERT OR IGNORE INTO staff_offices (office_name) VALUES (?)", (office_name,))
        self.connection.commit()

    def get_all_offices(self):
        self.cursor.execute("SELECT office_name FROM staff_offices")
        return [row["office_name"] for row in self.cursor.fetchall()]

    def add_student_hostel(self, hostel_name):
        """Inserts a new hostel config row into the lookup table."""
        self.cursor.execute("INSERT OR IGNORE INTO student_hostels (hostel_name) VALUES (?)", (hostel_name,))
        self.connection.commit()

    def get_all_hostels(self):
        """Fetches all available administrative hostel strings."""
        self.cursor.execute("SELECT hostel_name FROM student_hostels")
        return [row["hostel_name"] for row in self.cursor.fetchall()]

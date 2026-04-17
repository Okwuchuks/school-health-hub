CREATE TABLE IF NOT EXISTS students (
    student_id  INTEGER  PRIMARY KEY,
    first_name  TEXT  NOT NULL,
    middle_name TEXT,
    last_name  TEXT  NOT NULL,
    date_of_birth  TEXT  NOT NULL,
    enrollment_year  INTEGER NOT NULL,
    blood_group  TEXT  NOT NULL,
    gender  TEXT  NOT NULL,
    hostel  TEXT  NOT NULL,
    emergency_contact_name  TEXT NOT NULL,
    emergency_no  TEXT NOT NULL,
    is_active  BOOLEAN  NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS staff (
    staff_id  INTEGER PRIMARY KEY,
    first_name  TEXT  NOT NULL,
    middle_name  TEXT,
    last_name  TEXT  NOT NULL,
    date_of_birth  TEXT  NOT NULL,
    join_year  INTEGER  NOT NULL,
    blood_group  TEXT  NOT NULL,
    gender  TEXT  NOT NULL,
    staff_office  TEXT  NOT NULL,
    emergency_contact_name  TEXT  NOT NULL,
    emergency_no  TEXT  NOT NULL,
    is_active  BOOLEAN  NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS users(
    user_id  INTEGER  PRIMARY KEY,
    username  TEXT  NOT NULL  UNIQUE,
    password_hash  TEXT  NOT NULL,
    user_type  TEXT NOT NULL  DEFAULT  'user',
    status  TEXT   NOT NULL  DEFAULT  'pending',
    full_name  TEXT  NOT NULL,
    phone  TEXT  NOT NULL,
    gender  TEXT  NOT NULL,
    blood_group  TEXT NOT NULL,
    created_at  TEXT  NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    is_active   BOOLEAN  NOT NULL  DEFAULT 1
);

CREATE TABLE IF NOT EXISTS visits (
    visit_id  INTEGER  PRIMARY KEY,
    patient_type  TEXT  NOT NULL,
    patient_id  INTEGER  NOT NULL,
    user_id  INTEGER  NOT NULL,
    term  TEXT  NOT NULL,
    complaint  TEXT  NOT NULL,
    symptom_category  TEXT  NOT NULL,
    action_taken  TEXT  NOT NULL,
    visit_datetime  TEXT NOT NULL  DEFAULT  CURRENT_TIMESTAMP
);
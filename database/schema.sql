--School Health Hub (SHH)
--The blueprint for the tables.
--Author: Ifende Daniel



--Indicated tuple retrieval number adding a comment for easier work and flow
CREATE TABLE IF NOT EXISTS students (
    student_id  INTEGER  PRIMARY KEY, -- 0
    first_name  TEXT  NOT NULL, -- 1
    middle_name TEXT, -- 2
    last_name  TEXT  NOT NULL, -- 3
    date_of_birth  TEXT  NOT NULL, -- 4
    enrollment_year  INTEGER NOT NULL, -- 5
    blood_group  TEXT  NOT NULL, -- 6
    gender  TEXT  NOT NULL, -- 7
    hostel  TEXT  NOT NULL, -- 8
    emergency_contact_name  TEXT NOT NULL, -- 9
    emergency_no  TEXT NOT NULL, -- 10
    is_active  BOOLEAN  NOT NULL DEFAULT 1 -- 11
);

CREATE TABLE IF NOT EXISTS staff (
    staff_id  INTEGER PRIMARY KEY, -- 0
    first_name  TEXT  NOT NULL, -- 1
    middle_name  TEXT, -- 2
    last_name  TEXT  NOT NULL, -- 3
    date_of_birth  TEXT  NOT NULL, -- 4
    join_year  INTEGER  NOT NULL, -- 5
    blood_group  TEXT  NOT NULL, -- 6
    gender  TEXT  NOT NULL, -- 7
    staff_office  TEXT  NOT NULL, -- 8
    emergency_contact_name  TEXT  NOT NULL, -- 9
    emergency_no  TEXT  NOT NULL, -- 10
    is_active  BOOLEAN  NOT NULL DEFAULT 1, -- 11
    role TEXT NOT NULL -- 12
);

CREATE TABLE IF NOT EXISTS users(
    user_id  INTEGER  PRIMARY KEY, -- 0
    username  TEXT  NOT NULL  UNIQUE, -- 1
    password_hash  TEXT  NOT NULL, -- 2
    user_type  TEXT NOT NULL  DEFAULT  'user', -- 3
    first_name  TEXT  NOT NULL, -- 4
    last_name  TEXT  NOT NULL, -- 5
    phone  TEXT  NOT NULL, -- 6
    created_at  TEXT  NOT NULL  DEFAULT CURRENT_TIMESTAMP, -- 7
    is_active   BOOLEAN  NOT NULL  DEFAULT 1 -- 8
);

CREATE TABLE IF NOT EXISTS visits (
    visit_id  INTEGER  PRIMARY KEY, -- 0
    patient_type  TEXT  NOT NULL, -- 1
    patient_id  INTEGER  NOT NULL, -- 2
    user_id  INTEGER  NOT NULL, -- 3
    term  TEXT  NOT NULL, -- 4
    complaint  TEXT  NOT NULL, -- 5
    symptom_category  TEXT  NOT NULL, -- 6
    action_taken  TEXT  NOT NULL, -- 7
    visit_datetime  TEXT NOT NULL  DEFAULT  CURRENT_TIMESTAMP -- 8
);
"""
School Health Hub (SHH)
Functional Calculations used in the app.
Author: Ifende Daniel
"""

import datetime


def calculate_age(DOB_str):
    """
    [It calculates age based on the inputted date of birth]

    Args:
        DOB_str: [It is the date of birth inputted as a string]

    Returns:
        [Age]
    """

    birth_date = datetime.datetime.strptime(DOB_str, "%Y-%m-%d").date()
    today = datetime.date.today()

    age = today.year - birth_date.year

    has_had_birthday = (today.month, today.day) >= (birth_date.month, birth_date.day)
    if not has_had_birthday:
        age -= 1

    return age


def calculate_grade(enrollment_year):
    """
    [It calculates grade based on your enrollment year]

    Args:
        enrollment_year: [It is the year which someone was enrolled inputted as a string]

    Returns:
        [Grade]
    """

    grades = {1: "JSS 1", 2: "JSS 2", 3: "JSS 3", 4: "SSS 1", 5: "SSS 2", 6: "SSS 3"}

    today = datetime.date.today()
    month = today.month
    year = today.year

    if enrollment_year > year:
        return "Invalid"

    if month < 9:
        session_start = False
    else:
        session_start = True

    if session_start:
        yrs_spent = year - enrollment_year + 1
    else:
        yrs_spent = year - enrollment_year

    grade = grades.get(yrs_spent)

    if not grade:
        grade = "Graduated"

    return grade

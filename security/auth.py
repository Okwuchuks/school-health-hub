"""
School Health Hub (SHH)
This manages authorization and hashing of passwords as well as implementing a first user.
Author: Ifende Daniel
"""

import hashlib


def is_first_run(db_manager):
    users = db_manager.get_all_users()
    return len(users) == 0


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register_user(
    db_manager,
    username,
    password,
    user_type,
    first_name,
    last_name,
    phone,
):

    p_hash = hash_password(password)

    db_manager.create_user(
        username, p_hash, user_type, first_name, last_name, phone
    )


def verify_login(db_manager, username, password):
    _username = db_manager.get_user_by_username(username)

    if not _username:
        return False

    p_hash = hash_password(password)

    return p_hash == _username[2]

# Problem Statement

# You want to be safe online and use different passwords for different websites. However, you are forgetful at times and want to make a program that can match which password belongs to which website without storing the actual password!

# This can be done via something called hashing. Hashing is when we take something and convert it into a different, unique identifier. This is done using a hash function. Luckily, there are several resources that can help us with this.

# Solution

import hashlib

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

# Dictionary to simulate stored logins with hashed passwords
stored_logins = {
    "user1@example.com": hash_password("password123"),
    "user2@example.com": hash_password("mysecretpass"),
    "user3@example.com": hash_password("securepassword")
}

# check login credentials
def login(email: str, password_to_check: str) -> bool:
    if email in stored_logins:
        stored_password_hash = stored_logins[email]
        return stored_password_hash == hash_password(password_to_check)
    return False

email = input("Enter your email: ")
password_to_check = input("Enter your password: ")

if login(email, password_to_check):
    print("Login successful!")
else:
    print("Login failed. Please check your credentials.")

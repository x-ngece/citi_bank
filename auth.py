import bcrypt
import os
import datetime

LOG_FILE = "activity_log.txt"

# Function to log activities
def log_activity(activity):
    with open(LOG_FILE, "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} - {activity}\n")

# Function to hash passwords
def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)

# Function to check passwords
def check_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed)

# Function to validate email format
def validate_email(email):
    return "@" in email and "." in email

# Function to generate account number
def generate_account_number():
    return str(int(datetime.datetime.now().timestamp() * 1000))

# Function to register a new user
def register_user(first_name, last_name, email, password, confirm_password):
    if not validate_email(email):
        log_activity(f"Registration failed for {email}: Invalid email format.")
        return False, "Invalid email format."

    if len(password) < 8:
        log_activity(f"Registration failed for {email}: Password too short.")
        return False, "Password must be at least 8 characters."

    if password != confirm_password:
        log_activity(f"Registration failed for {email}: Passwords do not match.")
        return False, "Passwords do not match."

    account_number = generate_account_number()
    hashed_password = hash_password(password)

    user_data = f"{first_name},{last_name},{email},{hashed_password.decode()},{account_number}\n"

    if not os.path.exists("users.txt"):
        with open("users.txt", "w") as file:
            file.write(user_data)
    else:
        with open("users.txt", "a") as file:
            file.write(user_data)

    log_activity(f"User registered: {email} with account number {account_number}")
    return True, f"User registered successfully with account number: {account_number}"

# Function to login user
def login_user(email, password):
    if not os.path.exists("users.txt"):
        log_activity(f"Login attempt failed for {email}: No users registered.")
        return False, "No users registered yet."

    with open("users.txt", "r") as file:
        users = file.readlines()

    for user in users:
        user_data = user.strip().split(",")
        if user_data[2] == email and check_password(password, user_data[3].encode()):
            log_activity(f"User logged in: {email}")
            return True, f"Login successful! Welcome {user_data[0]} {user_data[1]}"

    log_activity(f"Login attempt failed for {email}: Invalid credentials.")
    return False, "Invalid email or password."

import re

class Validator:
    errors = []
    @staticmethod
    def is_valid_email(email):
        # Regular expression for basic email validation
        email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return 0 if re.match(email_pattern, email) else "Invalid email address"

    @staticmethod
    def is_valid_password(password):
        # Regular expression for password validation:
        # - At least 8 characters
        # - At least one lowercase letter
        # - At least one uppercase letter
        # - At least one digit
        password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$'
        
        if re.match(password_pattern, password):
            return 0
        else:
            error_message = "Password must meet the following criteria:\n"
            if len(password) < 8:
                error_message += "- Be at least 8 characters long\n"
            if not any(char.islower() for char in password):
                error_message += "- Contain at least one lowercase letter\n"
            if not any(char.isupper() for char in password):
                error_message += "- Contain at least one uppercase letter\n"
            if not any(char.isdigit() for char in password):
                error_message += "- Contain at least one digit\n"
                
            return error_message

    def password_match(password, confirmation):
        return 0 if password==confirmation else "Passwords do not match"
    @staticmethod
    def is_valid_username(username):
        # Regular expression for username validation:
        # - At least 5 characters
        # - Only alphanumeric characters
        username_pattern = r'^[a-zA-Z0-9]{5,}$'
        return 0 if re.match(username_pattern, username) else "Invalid username. It must be at least 5 characters long and consist of alphanumeric characters only"

    @staticmethod
    def is_empty(anyInput):
        return 0 if anyInput.strip()!="" else "All fields are required"

    def is_valid_usertype(usertype):
        return 0 if usertype in ("student", "facilitator", "admin") else "Please select a user type"
        # print(usertype)
    

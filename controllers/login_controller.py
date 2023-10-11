import sys
sys.path.append('views')
sys.path.append('models')
from tkinter import messagebox
from admin_view import AdminApp
from facilitator_view import FacilitatorLandingPageView
from login_view import LoginView
from validator import Validator
from database import Database
from authentication import Authentication
from student_view import StudentLandingPageView

class LoginController:
    def __init__(self, master, signup_callback, studentcallback=None):
        self.master = master
        self.signup_callback = signup_callback
        self.studentcallback = studentcallback
        self.view = LoginView(master, self.login, self.go_to_signup)
        self.realtimeValidation()
        self.db = Database()

        
    def realtimeValidation(self):
        # Bind events for real-time validation
        self.view.email_entry.bind("<KeyRelease>", lambda event: self.validate_entry(event, self.view.email_entry, Validator.is_valid_email))
        self.view.email_entry.bind("<FocusIn>", lambda event: self.validate_entry(event, self.view.email_entry, Validator.is_valid_email))
        self.view.email_entry.bind("<FocusOut>", lambda event: self.validate_entry(event, self.view.email_entry, Validator.is_valid_email))
        
        self.view.password_entry.bind("<KeyRelease>", lambda event: self.validate_entry(event, self.view.password_entry, Validator.is_valid_password))
        self.view.password_entry.bind("<FocusIn>", lambda event: self.validate_entry(event, self.view.password_entry, Validator.is_valid_password))
        self.view.password_entry.bind("<FocusOut>", lambda event: self.validate_entry(event, self.view.password_entry, Validator.is_valid_password))

    def validate_entry(self, event, entry, validation_func):
        input_value = entry.get()
        validation_result = validation_func(input_value)
        
        if validation_result == 0:
            entry.configure(font='times 24 bold', width=30, style='design2.TEntry')
            self.clear_error_message()
        else:
            entry.configure(font='times 24 bold', width=30, style='design1.TEntry')
            self.show_error_message(validation_result)

    def login(self):
        # Get user input from the view
        email = self.view.email_entry.get()
        password = self.view.password_entry.get()

        # Fetch user details for the given email
        query = "SELECT * FROM users WHERE email = ?"
        params = (email,)
        result = self.db.fetch_data(query, params)

        if result[0] == 0 and len(result[1]) > 0:
            user_info = result[1][0]

            # Extract user information
            user_id = user_info[0]
            full_name = user_info[1]
            username = user_info[2]
            email = user_info[3]
            user_type = user_info[5]

            hashed_password_from_db = user_info[4]

            # Verify the entered password against the hashed password from the database
            if Authentication.verify_password(password, hashed_password_from_db):
                # Login successful
                messagebox.showinfo("Successful Login", "You have successfully logged in!")

                # Additional actions after successful login...
                self.go_to_page(user_type)
            else:
                # Login failed (incorrect password)
                self.show_error_message("Invalid email or password")
        else:
            # Login failed (email not found)
            self.show_error_message("Invalid email or password")

    def go_to_page(self, user_type):
        # Assuming user_type is in the result
        if user_type == 'student':
            self.go_to_student()
        elif user_type == 'facilitator':
            self.go_to_facilitator()
            pass
        elif user_type == 'admin':
            self.go_to_admin()
    
    def go_to_signup(self):
        # Switch to the sign-up view
        self.signup_callback()

    def go_to_student(self):
        # Switch to the sign-up view
        StudentLandingPageView(self.master)
    
    def go_to_admin(self):
        # Switch to the sign-up view
        AdminApp(self.master)
    
    def go_to_facilitator(self):
        # Switch to the sign-up view
        class DataModel:
            def __init__(self):
                self.received_requests = [
                    {"student": "John", "request": "Please help with assignment 1."},
                    {"student": "Alice", "request": "I have a question about the lecture material."},
                ]
                self.sent_replies = []

            def add_reply(self, request, reply):
                self.sent_replies.append({"student": request["student"], "request": request["request"], "reply": reply})

        data_model = DataModel()
        FacilitatorLandingPageView(self.master, data_model)

    def show_error_message(self, message):
        self.view.error_message.config(text=message)
        
    def clear_error_message(self):
        self.view.error_message.config(text="")


import sys
from tkinter import messagebox, ttk
sys.path.append('views')
sys.path.append('models')
sys.path.append('utils')
sys.path.append('src')
from signup_view import SignUpView
from user_model import User
from validator import Validator

from database import Database
from authentication import Authentication

class SignUpController:
    def __init__(self, master, login_callback):
        self.master = master
        self.login_callback = login_callback
        self.view = SignUpView(master, self.signup, self.go_to_login)
        self.model = User("", "", "", "", "")
        self.realtimeValidation()
        self.db = Database()
        

    def realtimeValidation(self):
        # Bind events for real-time validation
        self.view.full_name_entry.bind("<KeyRelease>", lambda event: self.validate_entry(event, self.view.full_name_entry, Validator.is_empty))
        self.view.full_name_entry.bind("<FocusIn>", lambda event: self.validate_entry(event, self.view.full_name_entry, Validator.is_empty))
        self.view.full_name_entry.bind("<FocusOut>", lambda event: self.validate_entry(event, self.view.full_name_entry, Validator.is_empty))
        
        self.view.username_entry.bind("<KeyRelease>", lambda event: self.validate_entry(event, self.view.username_entry, Validator.is_valid_username))
        self.view.username_entry.bind("<FocusIn>", lambda event: self.validate_entry(event, self.view.username_entry, Validator.is_valid_username))
        self.view.username_entry.bind("<FocusOut>", lambda event: self.validate_entry(event, self.view.username_entry, Validator.is_valid_username))
        
        self.view.email_entry.bind("<KeyRelease>", lambda event: self.validate_entry(event, self.view.email_entry, Validator.is_valid_email))
        self.view.email_entry.bind("<FocusIn>", lambda event: self.validate_entry(event, self.view.email_entry, Validator.is_valid_email))
        self.view.email_entry.bind("<FocusOut>", lambda event: self.validate_entry(event, self.view.email_entry, Validator.is_valid_email))
        
        self.view.password_entry.bind("<KeyRelease>", lambda event: self.validate_entry(event, self.view.password_entry, Validator.is_valid_password))
        self.view.password_entry.bind("<FocusIn>", lambda event: self.validate_entry(event, self.view.password_entry, Validator.is_valid_password))
        self.view.password_entry.bind("<FocusOut>", lambda event: self.validate_entry(event, self.view.password_entry, Validator.is_valid_password))
        
        self.view.reenter_password_entry.bind("<KeyRelease>", lambda event: self.validate_password_match(event))
        self.view.reenter_password_entry.bind("<FocusIn>", lambda event: self.validate_password_match(event))
        self.view.reenter_password_entry.bind("<FocusOut>", lambda event: self.validate_password_match(event))

    def validate_password_match(self, event):
        password = self.view.password_entry.get()
        confirmation = self.view.reenter_password_entry.get()
        validation_result = Validator.password_match(password, confirmation)
        
        if validation_result == 0:
            self.view.reenter_password_entry.configure(font='times 8 bold', width=8, style='design2.TEntry')
            self.clear_error_message()
        else:
            self.view.reenter_password_entry.configure(font='times 8 bold', width=8, style='design1.TEntry')
            self.show_error_message(validation_result)

    def validate_entry(self, event, entry, validation_func):
        input_value = entry.get()
        validation_result = validation_func(input_value)
        
        if validation_result == 0:
            entry.configure(font='times 24 bold', width=30, style='design2.TEntry')
            self.clear_error_message()
        else:
            entry.configure(font='times 24 bold', width=30, style='design1.TEntry')
            self.show_error_message(validation_result)

        
    def show_error_message(self, message):
        self.view.error_message.config(text=message)
        
    def clear_error_message(self):
        self.view.error_message.config(text="")
    
    def register_user(self, full_name, username, email, password, user_type):
        hashed_password = Authentication.hash_password(password)
        query = "INSERT INTO users (full_name, username, email, password, user_type) VALUES (?, ?, ?, ?, ?)"
        params = (full_name, username, email, hashed_password, user_type)
        execute_query=self.db.execute_query(query, params)
    
        if execute_query[0]!=0:
            return[1, execute_query[1]]
        else:
            return [0]
    
    def signup(self):
        print('Signup pressed')
        # Perform final validation before submitting the form
        # This is just an example, you might need more complex validation logic here
        valid = self.validate_all_fields()
        if valid[0]:
            self.update_model()
            # signup logic here
            dbReg = self.register_user(self.model.full_name, 
                               self.model.username, self.model.email, self.model.password, self.model.user_type)
            if dbReg[0]==0:
                messagebox.showinfo("Succecful Signup", "You have Succefully signed up")
                self.go_to_login()
            else:
                messagebox.showerror("Database Error", dbReg[1])
        else:
            messagebox.showerror("Validation Error", valid[1])
    
    def validate_all_fields(self):
        validation_results = []

        # Validate full name
        full_name = self.view.full_name_entry.get()
        validation_results.append(Validator.is_empty(full_name))

        # Validate username
        username = self.view.username_entry.get()
        validation_results.append(Validator.is_valid_username(username))

        # Validate email
        email = self.view.email_entry.get()
        validation_results.append(Validator.is_valid_email(email))

        # Validate password
        password = self.view.password_entry.get()
        validation_results.append(Validator.is_valid_password(password))

        # Validate re-entered password
        confirmation = self.view.reenter_password_entry.get()
        validation_results.append(Validator.password_match(password, confirmation))

        # Validate user type
        usertype = self.view.user_type_var.get()
        validation_results.append(Validator.is_valid_usertype(usertype))
        print("usertype",usertype)

        # Check if any validation failed
        if any(result != 0 for result in validation_results):
            return False, validation_results
        else:
            return [True]

    
    def update_model(self):
        # Get user input from the view
        full_name = self.view.full_name_entry.get()
        username = self.view.username_entry.get()
        email = self.view.email_entry.get()
        password = self.view.password_entry.get()
        reenter_password = self.view.reenter_password_entry.get()
        user_type = self.view.user_type_var.get()
        
        # Update the model
        self.model.full_name = full_name
        self.model.username = username
        self.model.email = email
        self.model.password = password
        self.model.user_type = user_type
    
    def go_to_login(self):
        self.login_callback()

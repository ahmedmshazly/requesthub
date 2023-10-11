import tkinter as tk
from tkinter import ttk

class LoginView:
    def __init__(self, master, login_callback, signup_callback):
        self.master = master
        self.login_callback = login_callback
        self.signup_callback = signup_callback
        
                
        # Create labels and entry fields
        ttk.Label(master, text="email").pack(pady=(10, 0), anchor='w')  # Align labels to the left
        self.email_entry = ttk.Entry(master)
        self.email_entry.pack(pady=(0, 10), padx=10, fill=tk.X)
        
        ttk.Label(master, text="Password").pack(pady=(10, 0), anchor='w')
        self.password_entry = ttk.Entry(master, show="*")
        self.password_entry.pack(pady=(0, 10), padx=10, fill=tk.X)
        
        # Create log in button
        ttk.Button(master, text="Log In", command=self.login_callback).pack(pady=(10, 0), padx=10, fill=tk.X)
        
        # Create link to sign up page
        ttk.Label(master, text="Don't have an account?").pack(anchor='w')  # Align the label to the left
        ttk.Button(master, text="Sign Up", command=self.signup_callback).pack(pady=(0, 10), fill=tk.X)

        # Add an error message label
        self.error_message = ttk.Label(master, text="", foreground="red")
        self.error_message.pack(pady=(0, 10), padx=10, fill=tk.X, anchor='w')  # Align the error message to the left

        
def login_callback():
    print("Log In button clicked")

def signup_callback():
    print("Sign Up button clicked")

def main():
    root = tk.Tk()
    login_view = LoginView(root, login_callback, signup_callback)
    root.mainloop()

if __name__ == "__main__":
    main()

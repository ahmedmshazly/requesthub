import tkinter as tk
from tkinter import ttk

class SignUpView:
    def __init__(self, master, signup_callback, login_callback):
        self.master = master
        self.signup_callback = signup_callback
        self.login_callback = login_callback
        
        self.master.title("Sign Up")
        # self.master.geometry("400x400")
        self.master.configure(padx=20, pady=20)  # Added padding to the window
        
        self.style = ttk.Style()
        self.style.configure('TLabel', font=('Helvetica', 14))  # Increased font size
        self.style.configure('TEntry', font=('Helvetica', 8), padding=(5, 5))
        self.style.configure('TButton', font=('Helvetica', 12), padding=(5, 5), foreground='white', background='#4CAF50')  # Styled button
        self.style.theme_use('clam')
        self.style.configure('design2.TEntry', foreground='black', selectborderwidth=5, selectbackground='green', selectforeground='green')
        self.style.configure('design1.TEntry', foreground='black', fieldbackground='red', bordercolor='red')
        # Create labels and entry fields
        ttk.Label(master, text="Full Name").pack(pady=(10, 0), anchor='w')  # Align labels to the left
        self.full_name_entry = ttk.Entry(master)
        self.full_name_entry.pack(pady=(0, 10), padx=10, fill=tk.X)
        
        ttk.Label(master, text="Username").pack(pady=(10, 0), anchor='w')
        self.username_entry = ttk.Entry(master)
        self.username_entry.pack(pady=(0, 10), padx=10, fill=tk.X)
        
        ttk.Label(master, text="Email Address").pack(pady=(10, 0), anchor='w')
        self.email_entry = ttk.Entry(master)
        self.email_entry.pack(pady=(0, 10), padx=10, fill=tk.X)
        
        ttk.Label(master, text="Password").pack(pady=(10, 0), anchor='w')
        self.password_entry = ttk.Entry(master, show="*")
        self.password_entry.pack(pady=(0, 10), padx=10, fill=tk.X)
        
        ttk.Label(master, text="Re-enter Password").pack(pady=(10, 0), anchor='w')
        self.reenter_password_entry = ttk.Entry(master, show="*")
        self.reenter_password_entry.pack(pady=(0, 10), padx=10, fill=tk.X)
        
        # Create radio buttons for user type
        self.user_type_var = tk.StringVar()
        ttk.Radiobutton(master, text="Student", variable=self.user_type_var, value="student").pack(pady=(10, 5), anchor='w')
        ttk.Radiobutton(master, text="Facilitator", variable=self.user_type_var, value="facilitator").pack(pady=(0, 10), anchor='w')
        ttk.Radiobutton(master, text="Admin", variable=self.user_type_var, value="admin").pack(pady=(0, 10), anchor='w')
        
        # Create sign up button
        ttk.Button(master, text="Sign Up", command=self.signup_callback).pack(pady=(10, 0), padx=10, fill=tk.X)
        
        # Create link to login page
        ttk.Label(master, text="Already have an account?").pack(anchor='w')  # Align the label to the left
        ttk.Button(master, text="Log In", command=self.login_callback).pack(pady=(0, 10), fill=tk.X)

        # Add an error message label
        self.error_message = ttk.Label(master, text="", foreground="red")
        self.error_message.pack(pady=(0, 10), padx=10, fill=tk.X, anchor='w')  # Align the error message to the left
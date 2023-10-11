import tkinter as tk
from tkinter import ttk
import sys
sys.path.append('controllers')
# Assuming your controllers are in the 'controllers' directory
from signup_controller import SignUpController
from login_controller import LoginController

class SignUpView(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)

        self.geometry("600x900")
        
        
        SignUpController(self, self.go_to_login)

        # Assuming you have a close button in your SignUpView
        close_button = ttk.Button(self, text="Close", command=self.close)
        close_button.pack()
    
    def go_to_login(self):
        self.destroy()
        self.login_view = LoginView(self.master)

    def close(self):
        self.close_callback()
        self.destroy()

class LoginView(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)


        self.geometry("600x900")

        LoginController(self, self.go_to_signup)

        # Assuming you have a close button in your LoginView
        close_button = ttk.Button(self, text="Close", command=self.close)
        close_button.pack()
    
    def go_to_signup(self):
        self.destroy()
        self.signup_view = SignUpView(self.master)
    
    def close(self):
        self.close_callback()
        self.destroy()




class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Request Hub")
        self.geometry("0x0")
        self.minsize()

        SignUpView(self, )        
        style = ttk.Style()
        style.configure('Main.TFrame', background='white')

        main_frame = ttk.Frame(self, style='Main.TFrame')
        main_frame.pack(fill=tk.BOTH, expand=True)
        main_frame.configure(padding=(20, 20))

    

    def signup_callback(self):
        print("Sign Up button clicked")

    def login_callback(self):
        print("Log In button clicked")

    def close_signup(self):
        self.signup_view = None

    def close_login(self):
        self.login_view = None

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()

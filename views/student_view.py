import tkinter as tk
from tkinter import ttk, messagebox

class StudentLandingPageView(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)

        # Simulated student requests and feedback
        self.student_data = {
            "testuser": {
                "requests": [],
                "feedback": []
            }
        }

        self.geometry("600x900")

        self.style = ttk.Style()
        self.style.configure("TLabel", foreground="black")
        self.style.configure("TButton", background="#008CBA", foreground="white")
        self.style.configure("TFrame", background="#F0F0F0")

        self.create_widgets()

    def create_widgets(self):
        student_landing_frame = ttk.Frame(self)
        student_landing_frame.pack(padx=20, pady=20)

        student_label = ttk.Label(student_landing_frame, text="Student Landing Page", font=("Arial", 14, "bold"))
        student_label.grid(row=0, column=0, columnspan=2, pady=10)

        new_request_button = ttk.Button(student_landing_frame, text="New Request", command=self.show_new_request_form)
        new_request_button.grid(row=1, column=0, padx=5, pady=10)

        sent_requests_button = ttk.Button(student_landing_frame, text="Sent Requests", command=self.show_sent_requests)
        sent_requests_button.grid(row=1, column=1, padx=5, pady=10)

        feedback_button = ttk.Button(student_landing_frame, text="Feedback Received", command=self.show_feedback)
        feedback_button.grid(row=2, column=0, columnspan=2, pady=10)

    def show_new_request_form(self):
        new_request_window = tk.Toplevel(self)
        new_request_window.title("New Request Form")

        form_frame = ttk.Frame(new_request_window)
        form_frame.pack(padx=20, pady=10)

        facilitator_label = ttk.Label(form_frame, text="Facilitator's Username:")
        facilitator_label.grid(row=0, column=0, sticky="w")

        facilitator_entry = ttk.Entry(form_frame)
        facilitator_entry.grid(row=0, column=1, padx=5, pady=5)

        student_name_label = ttk.Label(form_frame, text="Your Name:")
        student_name_label.grid(row=1, column=0, sticky="w")

        student_name_entry = ttk.Entry(form_frame)
        student_name_entry.grid(row=1, column=1, padx=5, pady=5)

        subject_label = ttk.Label(form_frame, text="Subject:")
        subject_label.grid(row=2, column=0, sticky="w")

        subject_entry = ttk.Entry(form_frame)
        subject_entry.grid(row=2, column=1, padx=5, pady=5)

        request_label = ttk.Label(form_frame, text="Request:")
        request_label.grid(row=3, column=0, sticky="w")

        request_entry = tk.Text(form_frame, height=5, width=30)
        request_entry.grid(row=3, column=1, padx=5, pady=5)

        submit_button = ttk.Button(form_frame, text="Submit Request", command=lambda: self.submit_request(facilitator_entry.get(), student_name_entry.get(), subject_entry.get(), request_entry.get("1.0", tk.END), new_request_window))
        submit_button.grid(row=4, columnspan=2, pady=10)

    def submit_request(self, facilitator, student_name, subject, request, window):
        student_username = "testuser"  # Replace with the actual student's username
        if student_username not in self.student_data:
            self.student_data[student_username] = {"requests": [], "feedback": []}

        request_info = f"Facilitator: {facilitator}\nSubject: {subject}\nRequest: {request}"
        self.student_data[student_username]["requests"].append(request_info)

        messagebox.showinfo("Success", "Request submitted", icon="info")

        window.destroy()

    def show_sent_requests(self):
        sent_requests_window = tk.Toplevel(self)
        sent_requests_window.title("Sent Requests")

        student_username = "testuser"  # Replace with the actual student's username

        requests = self.student_data.get(student_username, {}).get("requests", [])

        if not requests:
            ttk.Label(sent_requests_window, text="No sent requests yet.", foreground="gray").pack(padx=20, pady=10)
        else:
            for request in requests:
                ttk.Label(sent_requests_window, text=request, foreground="blue").pack(padx=20, pady=5)

    def show_feedback(self):
        feedback_window = tk.Toplevel(self)
        feedback_window.title("Feedback Received")

        student_username = "testuser"  # Replace with the actual student's username

        feedback = self.student_data.get(student_username, {}).get("feedback", [])

        if not feedback:
            ttk.Label(feedback_window, text="No feedback received yet.", foreground="gray").pack(padx=20, pady=10)
        else:
            for fb in feedback:
                ttk.Label(feedback_window, text=fb, foreground="green").pack(padx=20, pady=5)

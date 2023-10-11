import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class AdminApp(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.root=self
        self.root.title("Admin Landing Page")

        # Create a tabbed interface
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Create tabs for Requests, Feedbacks, and Tasks
        self.requests_frame = ttk.Frame(self.notebook)
        self.feedbacks_frame = ttk.Frame(self.notebook)
        self.tasks_frame = ttk.Frame(self.notebook)

        self.notebook.add(self.requests_frame, text="Requests")
        self.notebook.add(self.feedbacks_frame, text="Feedbacks")
        self.notebook.add(self.tasks_frame, text="Tasks")

        # Requests tab
        self.requests_label = ttk.Label(self.requests_frame, text="All Student Requests", font=("Helvetica", 12, "bold"))
        self.requests_label.grid(row=0, column=0, columnspan=2, pady=(10, 5))

        self.requests_listbox = tk.Listbox(self.requests_frame, width=40, height=10)
        self.requests_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=5)
        self.populate_requests()  # Populate requests data

        self.view_request_button = ttk.Button(self.requests_frame, text="View Request", command=self.view_request)
        self.view_request_button.grid(row=2, column=0, padx=10, pady=5)

        # Feedbacks tab
        self.feedbacks_label = ttk.Label(self.feedbacks_frame, text="All Facilitator Feedbacks", font=("Helvetica", 12, "bold"))
        self.feedbacks_label.grid(row=0, column=0, columnspan=2, pady=(10, 5))

        self.feedbacks_listbox = tk.Listbox(self.feedbacks_frame, width=40, height=10)
        self.feedbacks_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=5)
        self.populate_feedbacks()  # Populate feedbacks data

        self.view_feedback_button = ttk.Button(self.feedbacks_frame, text="View Feedback", command=self.view_feedback)
        self.view_feedback_button.grid(row=2, column=0, padx=10, pady=5)

        # Tasks tab
        self.tasks_label = ttk.Label(self.tasks_frame, text="Administrative Tasks", font=("Helvetica", 12, "bold"))
        self.tasks_label.grid(row=0, column=0, columnspan=2, pady=(10, 5))

        self.tasks_listbox = tk.Listbox(self.tasks_frame, width=40, height=10)
        self.tasks_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        self.add_comment_button = ttk.Button(self.tasks_frame, text="Add Comment", command=self.add_comment)
        self.add_comment_button.grid(row=2, column=0, padx=10, pady=5)

        self.load_sample_data()  # Populate tasks data

    def populate_requests(self):
        # Sample student requests
        self.requests_data = {
            "Request 1": "Feedback 1",
            "Request 2": "Feedback 2",
            "Request 3": "Feedback 3"
        }

        for request in self.requests_data:
            self.requests_listbox.insert(tk.END, request)

    def populate_feedbacks(self):
        # Sample facilitator feedbacks
        self.feedbacks_data = {
            "Request 1": "Feedback 1",
            "Request 2": "Feedback 2",
            "Request 3": "Feedback 3"
        }

        for feedback in self.feedbacks_data:
            self.feedbacks_listbox.insert(tk.END, feedback)

    def view_request(self):
        selected_request = self.requests_listbox.get(self.requests_listbox.curselection())
        feedback = self.requests_data.get(selected_request, "No feedback available.")
        messagebox.showinfo("View Request", f"Selected Request: {selected_request}\nFeedback: {feedback}")

    def view_feedback(self):
        selected_request = self.feedbacks_listbox.get(self.feedbacks_listbox.curselection())
        feedback = self.feedbacks_data.get(selected_request, "No feedback available.")
        messagebox.showinfo("View Feedback", f"Selected Request: {selected_request}\nFeedback: {feedback}")

    def add_comment(self):
        selected_task = self.tasks_listbox.get(self.tasks_listbox.curselection())
        comment = simple_input_dialog("Add Comment", "Enter your comment:")
        if comment:
            messagebox.showinfo("Comment Added", f"Comment added to {selected_task}:\n{comment}")

    def load_sample_data(self):
        # Sample administrative tasks
        sample_tasks = ["Task 1", "Task 2", "Task 3", "Task 4", "Task 5"]

        for task in sample_tasks:
            self.tasks_listbox.insert(tk.END, task)

def simple_input_dialog(title, prompt):
    dialog = tk.Toplevel()
    dialog.title(title)

    label = ttk.Label(dialog, text=prompt)
    label.pack(padx=10, pady=5)

    entry = ttk.Entry(dialog)
    entry.pack(padx=10, pady=5)

    def return_input():
        dialog.destroy()

    ok_button = ttk.Button(dialog, text="OK", command=return_input)
    ok_button.pack(padx=10, pady=5)

    dialog.wait_window(dialog)

    return entry.get()

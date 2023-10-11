import tkinter as tk
from tkinter import ttk, messagebox

class FacilitatorLandingPageView(tk.Toplevel):
    def __init__(self, master, data_model):
        super().__init__(master)
        self.data_model = data_model

        self.title("Facilitator Landing Page")

        style = ttk.Style()
        style.configure("TButton", padding=5, font=("Helvetica", 12))

        self.requests_listbox = tk.Listbox(self, selectbackground="#E1E1E1")
        self.requests_listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        self.requests_listbox.bind("<<ListboxSelect>>", self.view_selected_request)

        view_button = ttk.Button(self, text="View Request", command=self.view_selected_request)
        view_button.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)

        sent_replies_button = ttk.Button(self, text="View Sent Replies", command=self.view_sent_replies)
        sent_replies_button.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)

        self.main_landing_page()

    def main_landing_page(self):
        self.requests_listbox.delete(0, tk.END)

        for request in self.data_model.received_requests:
            self.requests_listbox.insert(tk.END, f"Request from {request['student']}")

    def view_request_details(self, request):
        details_window = tk.Toplevel(self)
        details_window.title(f"Request from {request['student']}")

        request_label = tk.Label(details_window, text="Request:")
        request_label.pack()

        request_text = tk.Text(details_window, width=40, height=5)
        request_text.insert(tk.END, request["request"])
        request_text.config(state=tk.DISABLED)
        request_text.pack()

        reply_label = tk.Label(details_window, text="Reply:")
        reply_label.pack()

        reply_text = tk.Text(details_window, width=40, height=5)
        reply_text.pack()

        def send_reply():
            reply = reply_text.get("1.0", "end-1c")
            if reply:
                self.data_model.add_reply(request, reply)
                details_window.destroy()
                self.main_landing_page()

        reply_button = tk.Button(details_window, text="Send Reply", command=send_reply)
        reply_button.pack()

    def view_selected_request(self, event=None):
        selected_index = self.requests_listbox.curselection()
        if selected_index:
            request = self.data_model.received_requests[selected_index[0]]
            self.view_request_details(request)

    def view_sent_replies(self):
        sent_replies_window = tk.Toplevel(self)
        sent_replies_window.title("Sent Replies")

        for reply in self.data_model.sent_replies:
            reply_text = f"Reply to {reply['student']}:\n{reply['reply']}"
            reply_label = tk.Label(sent_replies_window, text=reply_text)
            reply_label.pack()

import tkinter as tk
from tkinter import messagebox
from database import user_authentication, fetch_contacts

class Dashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Contact Dashboard")
        self.geometry("600x400")

        self.login_frame = tk.Frame(self)
        self.login_frame.pack(pady=20)

        tk.Label(self.login_frame, text="Username").grid(row=0, column=0)
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.grid(row=0, column=1)

        tk.Label(self.login_frame, text="Password").grid(row=1, column=0)
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=1, column=1)

        self.login_button = tk.Button(self.login_frame, text="Login", command=self.authenticate_user)
        self.login_button.grid(row=2, columnspan=2)

        self.contact_frame = tk.Frame(self)

    def authenticate_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        try:
            if user_authentication(username, password):
                self.login_frame.destroy()
                self.display_contacts()
            else:
                messagebox.showerror("Authentication Error", "Invalid username or password")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def display_contacts(self):
        self.contact_frame.pack(pady=20)
        try:
            contacts = fetch_contacts()  # Assuming fetch_contacts function is implemented in database.py
            for idx, contact in enumerate(contacts, start=1):
                tk.Label(self.contact_frame, text=f"Contact {idx}: {contact['name']} - {contact['email']}").pack()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    app = Dashboard()
    app.mainloop()

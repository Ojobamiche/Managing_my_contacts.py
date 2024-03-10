import sqlite3
import tkinter as tk
from datetime import datetime

def create_tables():
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS user_credentials (
            username TEXT PRIMARY KEY,
            password_hash TEXT
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS contact_information (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            phone_number TEXT
        )
    ''')
    conn.commit()
    conn.close()

def user_authentication(username, password):
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute('SELECT * FROM user_credentials WHERE username=?', (username,))
    user = c.fetchone()
    conn.close()
    if user and check_password_hash(user[1], password):
        return True
    return False

def check_password_hash(saved_hash, password):
    # Implement hash comparison here
    return saved_hash == hash(password)

def fetch_contacts(user_id):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contact_information WHERE user_id=?", (user_id,))
    contacts = cursor.fetchall()
    conn.close()
    return contacts

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
        if user_authentication(username, password):
            self.login_frame.destroy()
            self.display_contacts()
        else:
            tk.messagebox.showerror("Authentication Error", "Invalid username or password")

    def display_contacts(self):
        self.contact_frame.pack(pady=20)
        # Assuming you have user_id available here
        contacts = fetch_contacts(user_id)
        for idx, contact in enumerate(contacts, start=1):
            tk.Label(self.contact_frame, text=f"Contact {idx}: {contact['name']} - {contact['email']}").pack()

if __name__ == "__main__":
    create_tables()
    app = Dashboard()
    app.mainloop()

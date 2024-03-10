from datetime import datetime
import sqlite3

def record_login_time(username):
    # Connect to the database
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    # Get the current time
    login_time = datetime.now()

    # Update the user's login time in the database
    cursor.execute("UPDATE user_credentials SET login_time=? WHERE username=?", (login_time, username))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def record_logout_time(username):
    # Connect to the database
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    # Get the current time
    logout_time = datetime.now()

    # Update the user's logout time in the database
    cursor.execute("UPDATE user_credentials SET logout_time=? WHERE username=?", (logout_time, username))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

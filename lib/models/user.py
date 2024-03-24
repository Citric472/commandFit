import sqlite3
import hashlib

class User:
    def __init__(self, username, email, password_hash):
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.logged_in = False

    def save(self):
        # Validate input
        if not self.validate():
            return False

        # Connect to the database
        conn = sqlite3.connect('commandfit.db')
        c = conn.cursor()

        # Insert the user into the users table
        c.execute("INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)",
                  (self.username, self.email, self.password_hash))

        # Commit changes and close connection
        conn.commit()
        conn.close()

        return True
    def register_user(username, email, password_hash):
       conn = sqlite3.connect('commandfit.db')
       c = conn.cursor()

    # Check if the email already exists
       c.execute("SELECT * FROM users WHERE email = ?", (email,))
       existing_user = c.fetchone()

       if existing_user:
           print("Error: This email address is already registered.")
           conn.close()
           return False

    # Insert the new user record
       c.execute("INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)",
              (username, email, password_hash))
       conn.commit()
       conn.close()
       return True

    
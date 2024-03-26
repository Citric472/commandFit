import argparse
import sqlite3
import hashlib

# Database setup
conn = sqlite3.connect('commandfit.db')
c = conn.cursor()

# Create users table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              username TEXT UNIQUE NOT NULL,
              email TEXT UNIQUE NOT NULL,
              password_hash TEXT NOT NULL)''')
conn.commit()

conn.close()

def register():
    print("Registering a new user...")
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")

    # Hash the password
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    # Connect to the database
    conn = sqlite3.connect('commandfit.db')
    c = conn.cursor()

    # Insert the user into the users table
    c.execute("INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)",
              (username, email, password_hash))

    # Commit changes and close connection
    conn.commit()
    conn.close()

    print("User registered successfully!")

def view_users():
    print("Viewing all users in the database...")
    
    # Connect to the database
    conn = sqlite3.connect('commandfit.db')
    c = conn.cursor()

    # Query the database to retrieve all users
    c.execute("SELECT * FROM users")
    users = c.fetchall()

    # Print the details of each user
    for user in users:
        print("User ID:", user[0])
        print("Username:", user[1])
        print("Email:", user[2])
        print()  # Print an empty line between users

    # Close the database connection
    
def delete_user():
    print("Deleting a user...")
    user_id = input("Enter the ID of the user you want to delete: ")

    # Connect to the database
    conn = sqlite3.connect('commandfit.db')
    c = conn.cursor()

    # Check if the user exists before deleting
    c.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = c.fetchone()
    if user:
        # If the user exists, confirm deletion
        confirm = input("Are you sure you want to delete user {}? (yes/no): ".format(user[1]))
        if confirm.lower() == 'yes':
            # Delete the user
            c.execute("DELETE FROM users WHERE id = ?", (user_id,))
            print("User {} deleted successfully.".format(user[1]))
        else:
            print("Deletion canceled.")
    else:
        print("Error: User with ID {} not found.".format(user_id))

def view_plans():
    print("Viewing available workout plans...")
    conn = sqlite3.connect('commandfit.db')
    c = conn.cursor()
    c.execute("SELECT * FROM workout_plans")
    plans = c.fetchall()
    if plans:
        print("Available Workout Plans:")
        for plan in plans:
            print(f"ID: {plan[0]}, Name: {plan[2]}")
    else:
        print("No workout plans found.")



# def view_plan():
#     print("Viewing details of a specific workout plan...")
#     plan_id = input("Enter the ID of the workout plan: ")

#     # Connect to the database
#     conn = sqlite3.connect('commandfit.db')
#     c = conn.cursor()

#     # Query the database for the details of the specified workout plan
#     c.execute("SELECT * FROM workout_plans WHERE id = ?", (plan_id,))
#     plan = c.fetchone()

#     # Close the database connection
#     conn.close()

#     if plan:
#         print("Workout Plan ID:", plan[0])
#         print("User ID:", plan[1])
#         print("Name:", plan[2])
#         # Add other details as needed
#     else:
#         print("Error: Workout plan with ID {} not found.".format(plan_id))

# def log_exercise():
#     print("Logging exercises completed during a workout session...")
#     # Add your log exercise logic here
#     exercise_name = input("Enter the name of the exercise: ")
#     sets = input("Enter the number of sets: ")
#     reps = input("Enter the number of reps: ")
#     weight_lifted = input("Enter the weight lifted (if applicable): ")
#     notes = input("Enter any additional notes (optional): ")
#     # Log the exercise details into the database or perform any other necessary action

def set_goal():
    print("Setting fitness goals...")
    # Add your set goal logic here
    goal_type = input("Enter the type of goal (e.g., Weight loss, Muscle gain): ")
    target_metric = input("Enter the target metric (e.g., Lose 10 pounds, Gain 5 pounds of muscle): ")
    target_deadline = input("Enter the target deadline (e.g., 2024-06-30): ")
    # Store the goal details in the database or perform any other necessary action
    print("Goal set successfully!")

def help_menu():
    print("""
Available commands:
1. Register a new user
2. View all users
3. Delete user
4. View plan          
5. Set fitness goals
6. View help menu
    """)

def main():
    while True:
        help_menu()
        choice = input("\nEnter the number of the command you want to execute (or 'exit' to quit): ")

        if choice == 'exit':
            break

        if choice == '1':
            register()
        elif choice == '2':
            view_users()
        elif choice == '3':
            delete_user()
        elif choice == '4':
            view_plans()
        elif choice == '5':
           set_goal()
        elif choice == '6':
            help_menu()
        
        
        else:
            print("Invalid command. Please enter a valid command number or type 'exit' to quit.")

if __name__ == "__main__":
    main()




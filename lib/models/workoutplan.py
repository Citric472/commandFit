import sqlite3

class WorkoutPlan:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def save(self):
        # Connect to the database
        conn = sqlite3.connect('commandfit.db')
        c = conn.cursor()

        # Insert the workout plan into the workout_plans table
        c.execute("INSERT INTO workout_plans (user_id, name) VALUES (?, ?)",
                  (self.user_id, self.name))

        # Commit changes and close connection
        conn.commit()
        conn.close()

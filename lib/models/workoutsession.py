import sqlite3

class WorkoutSession:
    def __init__(self, user_id, workout_plan_id):
        self.user_id = user_id
        self.workout_plan_id = workout_plan_id

    def save(self):
        # Connect to the database
        conn = sqlite3.connect('commandfit.db')
        c = conn.cursor()

        # Insert the workout session into the workout_sessions table
       

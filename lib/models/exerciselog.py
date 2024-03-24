import sqlite3

class ExerciseLog:
    def __init__(self, user_id, exercise_id, sets, reps, weight_lifted, notes):
        self.user_id = user_id
        self.exercise_id = exercise_id
        self.sets = sets
        self.reps = reps
        self.weight_lifted = weight_lifted
        self.notes = notes

    def save(self):
        # Connect to the database
        conn = sqlite3.connect('commandfit.db')
        c = conn.cursor()

        # Insert the exercise log into the exercise_logs table
        c.execute("INSERT INTO exercise_logs (user_id, exercise_id, sets, reps, weight_lifted, notes) VALUES (?, ?, ?, ?, ?, ?)",
                  (self.user_id, self.exercise_id, self.sets, self.reps, self.weight_lifted, self.notes))

        # Commit changes and close connection
        conn.commit()
        conn.close()

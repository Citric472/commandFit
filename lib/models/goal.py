import sqlite3

class Goal:
    def __init__(self, user_id, goal_type, target_metric, target_deadline):
        self.user_id = user_id
        self.goal_type = goal_type
        self.target_metric = target_metric
        self.target_deadline = target_deadline

    def save(self):
        # Connect to the database
        conn = sqlite3.connect('commandfit.db')
        c = conn.cursor()

        # Insert the goal into the goals table
        c.execute("INSERT INTO goals (user_id, goal_type, target_metric, target_deadline) VALUES (?, ?, ?, ?)",
                  (self.user_id, self.goal_type, self.target_metric, self.target_deadline))

        # Commit changes and close connection
        conn.commit()
        conn.close()

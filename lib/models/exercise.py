import sqlite3

class Exercise:
    def __init__(self, name, description, muscle_group, difficulty_level):
        self.name = name
        self.description = description
        self.muscle_group = muscle_group
        self.difficulty_level = difficulty_level

    def save(self):
        # Connect to the database
        conn = sqlite3.connect('commandfit.db')
        c = conn.cursor()

        # Insert the exercise into the exercises table
        c.execute("INSERT INTO exercises (name, description, muscle_group, difficulty_level) VALUES (?, ?, ?, ?)",
                  (self.name, self.description, self.muscle_group, self.difficulty_level))

        # Commit changes and close connection
        conn.commit()
        conn.close()

import sqlite3

# Connect to the database
conn = sqlite3.connect('commandfit.db')
c = conn.cursor()

# Create tables if they do not exist
c.execute('''CREATE TABLE IF NOT EXISTS users (
             id INTEGER PRIMARY KEY,
             username TEXT NOT NULL UNIQUE,
             email TEXT NOT NULL UNIQUE,
             password_hash TEXT NOT NULL
             )''')

c.execute('''CREATE TABLE IF NOT EXISTS exercises (
             id INTEGER PRIMARY KEY,
             name TEXT NOT NULL,
             description TEXT,
             muscle_group TEXT,
             difficulty_level TEXT
             )''')

c.execute('''CREATE TABLE IF NOT EXISTS exercise_logs (
             id INTEGER PRIMARY KEY,
             user_id INTEGER NOT NULL,
             exercise_id INTEGER NOT NULL,
             sets INTEGER,
             reps INTEGER,
             weight_lifted INTEGER,
             notes TEXT,
             FOREIGN KEY (user_id) REFERENCES users (id),
             FOREIGN KEY (exercise_id) REFERENCES exercises (id)
             )''')

c.execute('''CREATE TABLE IF NOT EXISTS goals (
             id INTEGER PRIMARY KEY,
             user_id INTEGER NOT NULL,
             goal_type TEXT,
             target_metric TEXT,
             target_deadline TEXT,
             FOREIGN KEY (user_id) REFERENCES users (id)
             )''')

c.execute('''CREATE TABLE IF NOT EXISTS workout_plans (
             id INTEGER PRIMARY KEY,
             user_id INTEGER NOT NULL,
             name TEXT,
             FOREIGN KEY (user_id) REFERENCES users (id)
             )''')

c.execute('''CREATE TABLE IF NOT EXISTS workout_sessions (
             id INTEGER PRIMARY KEY,
             user_id INTEGER NOT NULL,
             workout_plan_id INTEGER NOT NULL,
             FOREIGN KEY (user_id) REFERENCES users (id),
             FOREIGN KEY (workout_plan_id) REFERENCES workout_plans (id)
             )''')

# Seed initial data into the database
initial_data = [
    ('Cynthia', 'chepkemoicynthia@gmail.com', 'password123'),
    ('Krazy', 'krazyinn@gmail.com', 'password456')
]

# Seed initial data into the database
def seed_data():
    # Check if the users table is empty
    c.execute("SELECT COUNT(*) FROM users")
    count = c.fetchone()[0]
    if count == 0:
        for data in initial_data:
            try:
                c.execute("INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)", data)
            except sqlite3.IntegrityError as e:
                print(f"Error inserting user {data[0]}: {e}")
        conn.commit()
    else:
        print("Database already seeded with initial data.")

    # Seed exercises
    c.execute("INSERT INTO exercises (name, description, muscle_group, difficulty_level) VALUES (?, ?, ?, ?)",
              ('Push-up', 'Bodyweight exercise targeting the chest, shoulders, and triceps.', 'Upper body', 'Intermediate'))
    c.execute("INSERT INTO exercises (name, description, muscle_group, difficulty_level) VALUES (?, ?, ?, ?)",
              ('Squat', 'Compound exercise targeting the quadriceps, hamstrings, and glutes.', 'Lower body', 'Intermediate'))

    # Seed goals
    c.execute("INSERT INTO goals (user_id, goal_type, target_metric, target_deadline) VALUES (?, ?, ?, ?)",
              (1, 'Weight loss', 'Lose 10 pounds', '2024-06-30'))
    c.execute("INSERT INTO goals (user_id, goal_type, target_metric, target_deadline) VALUES (?, ?, ?, ?)",
              (2, 'Muscle gain', 'Gain 5 pounds of muscle', '2024-07-31'))

    # Seed workout plans
    c.execute("INSERT INTO workout_plans (user_id, name) VALUES (?, ?)",
              (1, 'Beginner Full Body Workout'))
    c.execute("INSERT INTO workout_plans (user_id, name) VALUES (?, ?)",
              (2, 'Advanced Upper/Lower Split'))

    # Seed exercise logs
    c.execute("INSERT INTO exercise_logs (user_id, exercise_id, sets, reps, weight_lifted, notes) VALUES (?, ?, ?, ?, ?, ?)",
              (1, 1, 3, 10, 0, 'Performed push-ups with good form.'))
    c.execute("INSERT INTO exercise_logs (user_id, exercise_id, sets, reps, weight_lifted, notes) VALUES (?, ?, ?, ?, ?, ?)",
              (1, 2, 3, 10, 0, 'Performed squats with proper depth.'))

    # Commit changes
    conn.commit()

# Execute seed_data function
seed_data()

# Close connection
conn.close()

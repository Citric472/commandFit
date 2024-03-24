# commandFit

CommandFit is a command-line interface (CLI) tool for fitness management. It allows users to register new accounts, log in to existing accounts, create workout plans, log exercises, set fitness goals, and more.

# Table of Contents
Installation
Usage
Commands
Configuration
Examples
Contributing
License
Installation
To install CommandFit, follow these steps:

# Clone the repository:

git clone https://github.com/yourusername/commandfit.git
# Navigate to the project directory:

cd commandfit
# Install dependencies:

pip install -r requirements.txt
# Usage
To use CommandFit, run the following command:

python3 cli.py

This will start the CLI interface and display a list of available commands.

Commands
CommandFit supports the following commands:

register: Register a new user account.
login: Log in to an existing user account.
logout: Log out from the current user session.
create-plan: Create a new workout plan.
view-plan: View details of a specific workout plan.
log-exercise: Log exercises completed during a workout session.
set-goal: Set fitness goals.
help: View the help menu.
Configuration
CommandFit does not require any configuration. However, users can customize settings such as database connections or default workout plans by modifying the config.py file.

python

# Sample configuration file (config.py)

DATABASE_URI = 'sqlite:///commandfit.db'
DEFAULT_WORKOUT_PLAN = 'beginner_plan'
Examples
Here are some examples of how to use CommandFit:


# Register a new user
python3 cli.py register

# Log in to an existing user account
python3 cli.py login

# Create a new workout plan
python3 cli.py create-plan

# Log exercises completed during a workout session
python3 cli.py log-exercise

# Contributing
Contributions to CommandFit are welcome! If you encounter any bugs or have suggestions for new features, please open an issue on the GitHub repository. Pull requests are also encouraged.

# License
This project is licensed under the MIT License
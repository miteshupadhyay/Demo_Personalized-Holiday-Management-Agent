# Project template initialization script - creates directory structure and empty files for holiday management project
import os
from pathlib import Path
import logging

# Configure logging to display timestamps and messages
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

# Define the root project name
project_name = "holiday_management"

# Define the complete directory and file structure for the project
list_of_files = [
    # Configuration directory
    f"{project_name}/config/settings.py",
    f"{project_name}/config/__init__.py"

    # Agents directory - contains different agent implementations
    f"{project_name}/agents/__init__.py",
    f"{project_name}/agents/planner.py",
    f"{project_name}/agents/researcher.py",

    # Teams directory - contains team configurations
    f"{project_name}/teams/__init__.py",
    f"{project_name}/teams/holiday_team.py",

    # Utils directory - contains utility functions
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/utils.py",

    # Root level application files
    "app.py",
    "tests.py"
]

# Iterate through each file path and create directories and files if they don't exist
for filepath in list_of_files:
    filepath = Path(filepath)
    # Example : File Path : holiday_management\config\settings.py


    # Split the filepath into directory and filename components
    filedir, filename = os.path.split(filepath)
    # Example FileDir : holiday_management\config

    # Create the directory structure if it doesn't already exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating dirctory : {filedir}")

    # Create empty file if it doesn't exist or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating file : {filepath}")
    else:
        # Log if the file already exists with content
        logging.info(f"File already exists : {filepath}")
    




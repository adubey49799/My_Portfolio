# ============================================================
# Lab 5: Data Loading and Storage
# Part 1: CSV Data Handling
# ============================================================

# Import pandas library for reading, modifying, and saving CSV files
import pandas as pd


# ------------------------------------------------------------
# Task 2: Upload/load the dataset into Jupyter Notebook using Pandas
# ------------------------------------------------------------

# Read the winequality-red.csv dataset
# Make sure winequality-red.csv is saved in the same folder as this Python file/notebook
df = pd.read_csv("winequality-red.csv")

# Display confirmation message and dataset size
print("Dataset loaded successfully.")
print("Number of rows and columns:", df.shape)

# Display the first 5 rows of the original dataset
print("\nFirst 5 rows of the original dataset:")
print(df.head())


# ------------------------------------------------------------
# Task 3: Add a new column to assign a unique ID to each row
# ------------------------------------------------------------

# Insert a new column named 'unique_id' as the first column
# The unique ID starts from 1 and continues until the last row
df.insert(0, "unique_id", range(1, len(df) + 1))

print("\nUnique ID column added successfully.")


# ------------------------------------------------------------
# Task 4: Display the first 10 rows of the updated DataFrame
# ------------------------------------------------------------

print("\nFirst 10 rows of the updated DataFrame:")
print(df.head(10))


# ------------------------------------------------------------
# Task 5: Export the modified DataFrame to a new CSV file
# ------------------------------------------------------------

# Save the updated DataFrame into a new CSV file
# index=False prevents Pandas from adding an extra index column
output_file = "winequality-red-with-id.csv"
df.to_csv(output_file, index=False)

print("\nModified CSV file exported successfully.")
print("Exported file name:", output_file)


# ------------------------------------------------------------
# Task 6: Confirm the exported CSV file can be read again
# ------------------------------------------------------------

# Read the exported CSV file again to verify it was created correctly
df_exported = pd.read_csv(output_file)

print("\nExported CSV file loaded again for verification.")
print("Number of rows and columns in exported file:", df_exported.shape)

print("\nFirst 10 rows from the exported CSV file:")
print(df_exported.head(10))

# ============================================================
# Lab 5: Data Loading and Storage
# Part 2: JSON Operations
# ============================================================

# Import the json library to work with JSON data
import json


# ------------------------------------------------------------
# Task 7: Convert a sample JSON string into a Python object
# ------------------------------------------------------------

# Create a sample JSON string
json_string = '''
{
    "student_name": "Alok Dubey",
    "course": "Data Science and Big Data Analytics",
    "lab": "Lab 5",
    "topic": "Data Loading and Storage",
    "completed": true
}
'''

# Convert JSON string into a Python dictionary
python_object = json.loads(json_string)

print("Task 7: JSON string converted into Python object")
print("Data type:", type(python_object))
print("Python object:")
print(python_object)


# ------------------------------------------------------------
# Task 8: Convert a Python object into JSON data
# ------------------------------------------------------------

# Create a Python dictionary
student_info = {
    "student_name": "Alok Dubey",
    "course": "Data Science and Big Data Analytics",
    "lab_number": 5,
    "topics": ["CSV Handling", "JSON Operations", "NBA API"],
    "submission_required": True
}

# Convert Python dictionary into JSON string
json_data = json.dumps(student_info)

print("\nTask 8: Python object converted into JSON data")
print("Data type:", type(json_data))
print("JSON data:")
print(json_data)


# ------------------------------------------------------------
# Task 9: Convert various Python objects into JSON strings
# ------------------------------------------------------------

# Different Python objects
python_dictionary = {"name": "LeBron James", "team": "Los Angeles Lakers"}
python_list = ["CSV", "JSON", "API", "Data Storage"]
python_tuple = ("Python", "Pandas", "JSON")
python_string = "Data Loading and Storage"
python_integer = 100
python_float = 95.75
python_boolean = True
python_none = None

# Convert and print each Python object as a JSON string
print("\nTask 9: Various Python objects converted into JSON strings")

print("Dictionary to JSON:", json.dumps(python_dictionary))
print("List to JSON:", json.dumps(python_list))
print("Tuple to JSON:", json.dumps(python_tuple))
print("String to JSON:", json.dumps(python_string))
print("Integer to JSON:", json.dumps(python_integer))
print("Float to JSON:", json.dumps(python_float))
print("Boolean to JSON:", json.dumps(python_boolean))
print("None to JSON:", json.dumps(python_none))


# ------------------------------------------------------------
# Task 10: Convert a Python dictionary into a sorted, formatted JSON string
# ------------------------------------------------------------

# Create a Python dictionary with unsorted keys
wine_sample = {
    "quality": 5,
    "alcohol": 9.4,
    "pH": 3.51,
    "density": 0.9978,
    "citric_acid": 0.00,
    "fixed_acidity": 7.4
}

# Convert dictionary into a formatted JSON string
# sort_keys=True sorts the dictionary keys alphabetically
# indent=4 formats the JSON with an indentation level of 4
formatted_json = json.dumps(wine_sample, sort_keys=True, indent=4)

print("\nTask 10: Sorted and formatted JSON string with indent level 4")
print(formatted_json)

# ============================================================
# Lab 5: Data Loading and Storage
# Part 3: Working with NBA API
# ============================================================

# ------------------------------------------------------------
# Task 11: Install the NBA API package
# ------------------------------------------------------------

# If nba_api is not already installed, run this command in a notebook cell:
# !pip install nba_api

# If running in VS Code terminal, use:
# pip install nba_api


# ------------------------------------------------------------
# Task 12: Get player and team IDs
# ------------------------------------------------------------

# Import players and teams modules from nba_api
from nba_api.stats.static import players
from nba_api.stats.static import teams

# Get the list of all NBA players
player_dict = players.get_players()

# Find LeBron James from the player list
bron = [player for player in player_dict if player["full_name"] == "LeBron James"][0]

# Store LeBron James player ID
bron_id = bron["id"]

print("LeBron James Information:")
print(bron)
print("LeBron James Player ID:", bron_id)


# Get the list of all NBA teams
team_dict = teams.get_teams()

# Find Golden State Warriors from the team list
GSW = [team for team in team_dict if team["full_name"] == "Golden State Warriors"][0]

# Store Golden State Warriors team ID
GSW_id = GSW["id"]

print("\nGolden State Warriors Information:")
print(GSW)
print("Golden State Warriors Team ID:", GSW_id)


# ------------------------------------------------------------
# Task 13: Collect game data for a player and export it to CSV
# ------------------------------------------------------------

# Import PlayerGameLog endpoint to collect player game data
from nba_api.stats.endpoints import playergamelog

# For this assignment, we will collect game data for LeBron James
# season="2023-24" means the 2023-2024 NBA season
# season_type_all_star="Regular Season" means regular season games only

game_log = playergamelog.PlayerGameLog(
    player_id=bron_id,
    season="2023-24",
    season_type_all_star="Regular Season"
)

# Convert the API result into a Pandas DataFrame
lebron_games_df = game_log.get_data_frames()[0]

# Display confirmation message
print("\nLeBron James game data collected successfully.")

# Display number of rows and columns
print("Number of rows and columns:", lebron_games_df.shape)

# Display the first 10 rows of the player game data
print("\nFirst 10 rows of LeBron James game data:")
print(lebron_games_df.head(10))


# ------------------------------------------------------------
# Export player game data to a CSV file
# ------------------------------------------------------------

# Save the game log data to a CSV file
nba_output_file = "lebron_james_game_data_2023_24.csv"
lebron_games_df.to_csv(nba_output_file, index=False)

print("\nNBA player game data exported successfully.")
print("Exported file name:", nba_output_file)


# ------------------------------------------------------------
# Verify the exported NBA CSV file
# ------------------------------------------------------------

# Read the exported CSV file again to verify successful export
nba_exported_df = pd.read_csv(nba_output_file)

print("\nExported NBA CSV file loaded again for verification.")
print("Number of rows and columns in exported NBA file:", nba_exported_df.shape)

print("\nFirst 10 rows from the exported NBA CSV file:")
print(nba_exported_df.head(10))
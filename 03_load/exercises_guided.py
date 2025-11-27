
# 03_LOAD - GUIDED EXERCISES (STEP BY STEP)
#
# Objective:
# - Learn how to save data in CSV, JSON, and Excel.
# - Learn how to handle paths and directories.
# - Create professional load functions.
#
# IMPORTANT:
# We will work with the file:
#   data/sample_to_save.csv


# 0 IMPORTS
#
# TASK:
# - Import pandas as pd
# - Import os (to create folders)
#
# HINT:
# import pandas as pd
# import os
#
# YOUR CODE HERE


# 1 EXERCISE 1 - LOAD THE BASE FILE
#
# File: data/sample_to_save.csv
#
# TASKS:
# 1. Load the file into a DataFrame named df.
# 2. Display:
#    - the first rows (head)
#    - DataFrame info (info)
#    - numerical description (describe)
#
# HINT:
# df = pd.read_csv("data/sample_to_save.csv")
#
# YOUR CODE HERE


# 2 EXERCISE 2 - SAVE AS CSV IN AN OUTPUT FOLDER
#
# OBJECTIVE:
# - Learn how to create folders and save files inside them.
#
# TASKS:
# 1. Create a folder named "output" inside the module.
# 2. Save the DataFrame as:
#       output/data_clean.csv
# 3. Do NOT include the index (index=False)
#
# HINTS:
# os.makedirs("output", exist_ok=True)
# df.to_csv("output/data_clean.csv", index=False)
#
# YOUR CODE HERE


# 3 EXERCISE 3 - SAVE AS JSON
#
# OBJECTIVE:
# - Export the DataFrame to JSON.
#
# TASKS:
# 1. Save the DataFrame as:
#       output/data_clean.json
# 2. Use "records" format.
# 3. Add indent=2 for readability.
#
# HINT:
# df.to_json("output/data_clean.json", orient="records", indent=2)
#
# YOUR CODE HERE


# 4 EXERCISE 4 - SAVE AS EXCEL
#
# OBJECTIVE:
# - Learn how to export DataFrames to Excel (.xlsx)
#
# TASKS:
# 1. Save the DataFrame as:
#       output/data_clean.xlsx
# 2. Do NOT include the index.
#
# HINT:
# df.to_excel("output/data_clean.xlsx", index=False)
#
# YOUR CODE HERE


# 5 EXERCISE 5 - SAVE MULTIPLE VERSIONS
#
# OBJECTIVE:
# - Learn how to save multiple versions (by date, number, etc.)
#
# TASKS:
# 1. Ask the user for a name or version (e.g., "v1")
# 2. Save the file as:
#       output/data_clean_VERSION.csv
# 3. Also save as JSON:
#       output/data_clean_VERSION.json
#
# OPTIONAL:
# - Auto-generate a version based on date/time.
#
# EXAMPLE:
# version = "v1"
# f"output/data_clean_{version}.csv"
#
# YOUR CODE HERE


# 6 EXERCISE 6 - CREATE A load_data() FUNCTION
#
# OBJECTIVE:
# - Simulate a professional Load module.
#
# TASK:
# 1. Create a function load_data(df, basename):
#       - df → DataFrame to save
#       - basename → base name for the files
# 2. The function must:
#       - create the output folder if it does not exist
#       - save CSV
#       - save JSON
#       - save Excel
# 3. Save files with the names:
#       output/BASENAME.csv
#       output/BASENAME.json
#       output/BASENAME.xlsx
#
# SUGGESTION:
# def load_data(df, basename):
#     ...
#
# YOUR CODE HERE


# 7 EXERCISE 7 - TEST THE load_data() FUNCTION
#
# TASKS:
# 1. Call load_data(df, "final_output")
# 2. Verify that the following were created in the output folder:
#       final_output.csv
#       final_output.json
#       final_output.xlsx
#
# YOUR CODE HERE


# FINAL EXERCISE
#
# OBJECTIVE:
# - Complete a mini professional Load step.
#
# TASKS:
# 1. Create a function save_with_date(df):
#       - generates a timestamp YYYYMMDD_HHMMSS
#       - saves the DataFrame as:
#           output/save_TIMESTAMP.csv
# 2. Call the function with df.
# 3. Verify that the file was created correctly.
#
# HINT:
# from datetime import datetime
# timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#
# YOUR CODE HERE



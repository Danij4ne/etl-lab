# MINI PROJECT 2 — ETL PIPELINE (API + CSV)
#
# Description:
# ETL pipeline focused on extracting data from a public API,
# combining it with a local CSV, and generating a unified output.
#
# Objective:
# - Practice ingesting data from APIs (GET requests).
# - Perform full transformations.
# - Export results in multiple formats.
#
# Note:
# This file only contains structure and tasks. No solutions.


# 0. REQUIRED IMPORTS
#
# Tasks:
# 1. Import requests (for the API)
# 2. Import pandas as pd
# 3. Import os (for paths / folders)
# 4. (Optional) Import datetime
#
# YOUR CODE HERE


# 1. EXTRACT FROM API
#
# Recommended API (DummyJSON):
#     https://dummyjson.com/users?limit=20
#
# It returns a JSON object with:
#   - A list of users
#   - Fields: id, firstName, lastName, age, email, etc.
#
# Tasks:
# 1. Create the function extract_api(url):
#       - Perform a GET request
#       - Check status_code
#       - Convert the response to a DataFrame
#       - Handle basic possible errors
#
# 2. Call extract_api(url) → df_api_users
#
# 3. Display:
#       - shape
#       - columns
#       - first rows
#
# YOUR CODE HERE


# 2. EXTRACT FROM LOCAL CSV
#
# Recommended file:
#     data/users.csv  (from mini project 1)
#
# Tasks:
# 1. Create the function extract_csv(path)
# 2. Load the CSV into df_local
# 3. Verify structure with:
#       df_local.info()
#
# YOUR CODE HERE


# 3. TRANSFORM
#
# Objective:
# Unify local data with API data.
#
# Considerations:
# - Columns may not match exactly.
# - You may need to rename columns.
# - You may need to create new columns.
# - You may need to convert types (str, int, bool).
#
# Tasks:
# 1. Create the function transform_data(df_api, df_local):
#       - Select relevant columns
#       - Rename columns to unify structure
#       - Create a "source" column indicating origin
#       - Concatenate the DataFrames
#       - Remove duplicates by email or id
#       - Reset the index
#
# 2. Store the result in df_final
#
# YOUR CODE HERE


# 4. LOAD
#
# Objective:
# Export final data in several formats.
#
# Tasks:
# 1. Create folder "output_api" if it does not exist
#
# 2. Create the function load_data(df, basename):
#       - Save CSV: output_api/BASENAME.csv
#       - Save JSON: output_api/BASENAME.json
#       - Save Excel: output_api/BASENAME.xlsx
#
# 3. Call:
#       load_data(df_final, "users_api_combined")
#
# 4. Check that all files have been created
#
# YOUR CODE HERE


# 5. FULL PIPELINE EXECUTION
#
# Tasks:
# 1. Call extract_api()
# 2. Call extract_csv()
# 3. Call transform_data()
# 4. Call load_data()
#
# HINT:
# df_api_users = extract_api(...)
# df_local = extract_csv(...)
# df_final = transform_data(df_api_users, df_local)
# load_data(df_final, "users_api_combined")
#
# YOUR CODE HERE


# 6. FINAL VALIDATION
#
# Tasks:
# - Show total number of combined records
# - Show the final columns
# - Show the first rows
#
# YOUR CODE HERE


 
# MINI PROJECT 1 — ETL PIPELINE (CSV + JSON)

# Description:
# Simple ETL pipeline that integrates data from:
#   - A local CSV file
#   - A local JSON file
#
# Objective:
#   - Practice a complete and modular ETL process.
#   - Consolidate reading, transformation, and loading.
#
# Note:
#   - This file contains only the structure and tasks.
#   - It does not include solutions.
 


 
# 0. REQUIRED IMPORTS
 
# Tasks:
# - Import pandas as pd
# - Import json if you consider it necessary
# - Import os (for paths or folders)
#
# YOUR CODE HERE


 
# 1. EXTRACT
 
# Objective: load data from a CSV and a JSON file.
#
# Expected inputs:
#   data/users.csv
#   data/users_extra.json
#
# Tasks:
# 1. Create the function extract_csv(path)
#       - It must read and return a DataFrame.
#
# 2. Create the function extract_json(path)
#       - It must read the JSON and return a DataFrame.
#       - It can use pandas.read_json or json.load.
#
# 3. Call both functions and store the results in:
#       df_csv
#       df_json
#
# 4. Check shapes and columns to verify consistency.
#
# YOUR CODE HERE


 
# 2. TRANSFORM
 
# Objective: unify and clean the data.
#
# Tasks:
# 1. Create the function transform_data(df_csv, df_json)
#       It must:
#       - Combine both DataFrames (row-wise or column-wise).
#       - Remove duplicates if they exist.
#       - Normalize column names (lowercase, no spaces).
#       - Convert ages to numeric type if necessary.
#       - Reorder columns if appropriate.
#
# 2. Store the result in the variable:
#       df_final
#
# 3. Review the shape and info of df_final to confirm integrity.
#
# YOUR CODE HERE


 
# 3. LOAD
 
# Objective: save the cleaned results in a final format.
#
# Tasks:
# 1. Create an "output" folder if it does not exist.
# 2. Create the function load_data(df, basename):
#       It must:
#       - Save CSV: output/BASENAME.csv
#       - Save JSON: output/BASENAME.json (records, indent=2)
#
# 3. Call load_data(df_final, "users_clean")
#
# 4. Check that the files have been generated correctly.
#
# YOUR CODE HERE


 
# 4. PIPELINE EXECUTION
 
# Objective: run the ETL end-to-end.
#
# Tasks:
# 1. Extract data
# 2. Transform data
# 3. Load the final data
#
# HINT:
# df_csv = extract_csv(...)
# df_json = extract_json(...)
# df_final = transform_data(df_csv, df_json)
# load_data(df_final, "users_clean")
#
# YOUR CODE HERE


 
# 5. FINAL VALIDATION
 
# Objective: allow review of the pipeline.
#
# Tasks:
# - Print the final number of records
# - Show the columns of the final DataFrame
# - (Optional) Show the first rows
#
# YOUR CODE HERE




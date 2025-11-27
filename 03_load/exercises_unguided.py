
# 03_LOAD - UNGUIDED EXERCISES
#
# Objective:
# - Practice the "L" part of ETL (Load) without step-by-step guidance.
# - Save DataFrames in different formats.
# - Work with paths, folders, filenames, and versioning.
#
# Base dataset:
# - data/sample_to_save.csv
#
# Recommendation:
# - Try to complete these exercises without looking at the guided ones.
# - If you get stuck, review the guided version to recall ideas.


# 0 IMPORTS
#
# TASK:
# 1. Import pandas as pd.
# 2. Import os to manage folders.
# 3. (Optional) Import datetime for timestamps.
#
# YOUR CODE HERE


# 1 EXERCISE 1 - LOAD THE BASE DATASET
#
# File: data/sample_to_save.csv
#
# TASKS:
# 1. Load the file into a DataFrame named df.
# 2. Verify:
#    - first rows
#    - shape
#    - data types
#
# YOUR CODE HERE


# 2 EXERCISE 2 - CREATE OUTPUT FOLDER
#
# TASKS:
# 1. Create a folder named "output" if it does not exist.
# 2. Check in your terminal or file explorer that it was created.
#
# NOTE:
# - Use the same "output" folder for all following exercises.
#
# YOUR CODE HERE


# 3 EXERCISE 3 - SAVE CSV WITH DIFFERENT SEPARATOR
#
# OBJECTIVE:
# - Practice using separators other than comma.
#
# TASKS:
# 1. Save the DataFrame df in:
#       output/data_semicolon.csv
# 2. Use ";" as the separator.
# 3. Do not save the index.
#
# QUESTION:
# - What changes when you open the file in a text editor?
#
# YOUR CODE HERE


# 4 EXERCISE 4 - SAVE JSON ORIENTED BY COLUMNS
#
# OBJECTIVE:
# - Try different JSON orientations.
#
# TASKS:
# 1. Save the DataFrame in:
#       output/data_by_columns.json
# 2. Use orient="columns" or any format different from "records".
# 3. Compare the result with a "records" JSON.
#
# YOUR CODE HERE


# 5 EXERCISE 5 - SAVE A SELECTION OF COLUMNS
#
# OBJECTIVE:
# - Learn to save only part of the DataFrame.
#
# TASKS:
# 1. Create a new DataFrame df_small with only:
#       - name
#       - email
# 2. Save df_small as:
#       output/data_contacts.csv
# 3. Do not save the index.
#
# YOUR CODE HERE


# 6 EXERCISE 6 - SAVE TO EXCEL WITH CUSTOM SHEET NAME
#
# OBJECTIVE:
# - Practice exporting to Excel with sheet_name.
#
# TASKS:
# 1. Save df as:
#       output/data_users.xlsx
# 2. Use a custom sheet name, for example: "Users".
#
# YOUR CODE HERE


# 7 EXERCISE 7 - CREATE A save_all_formats() FUNCTION
#
# OBJECTIVE:
# - Encapsulate saving logic.
#
# TASK:
# 1. Create a function named save_all_formats(df, basename) that:
#    - receives a DataFrame and a base name (string)
#    - saves:
#        output/BASENAME.csv
#        output/BASENAME.json
#        output/BASENAME.xlsx
#    - CSV without index
#    - JSON with orient="records" and indent=2
#    - Excel without index
# 2. Test the function with:
#    save_all_formats(df, "users_full")
#
# YOUR CODE HERE


# 8 EXERCISE 8 - CONTROL OVERWRITE
#
# OBJECTIVE:
# - Avoid unintentionally overwriting files.
#
# TASKS:
# 1. Create a function save_if_not_exists(df, path) that:
#    - receives a DataFrame and a file path (e.g., "output/users_safe.csv")
#    - if the file does NOT exist, saves it as CSV
#    - if the file DOES exist, prints:
#         "The file already exists. It has not been overwritten."
# 2. Test the function twice with the same path.
#
# YOUR CODE HERE


# 9 EXERCISE 9 - SAVE DIFFERENT VERSIONS WITH TIMESTAMP
#
# OBJECTIVE:
# - Learn to version outputs using date/time.
#
# TASKS:
# 1. Create a function save_with_timestamp(df, base_name) that:
#    - generates a timestamp in format: YYYYMMDD_HHMMSS
#    - creates a filename:
#         output/base_name_TIMESTAMP.csv
#    - saves the DataFrame using that filename.
# 2. Call the function multiple times and confirm that it creates different files.
#
# HINT:
# - from datetime import datetime
# - datetime.now().strftime("%Y%m%d_%H%M%S")
#
# YOUR CODE HERE


# 10 EXERCISE 10 - MINI LOAD PIPELINE
#
# OBJECTIVE:
# - Simulate the full "L" phase after an ETL.
#
# ASSUMPTION:
# - Imagine you already have two prepared DataFrames:
#     df_hw_final       -> cleaned height/weight data
#     df_clean_final    -> cleaned user data
#
# (If you do not have them, you may quickly recreate them by loading Transform outputs,
#  or reuse df twice with different names.)
#
# TASKS:
# 1. Create a function final_load_pipeline() that:
#    - receives two DataFrames: df_hw_final and df_clean_final
#    - creates a folder "output_final" if it does not exist
#    - saves:
#         output_final/heights_weights_final.csv
#         output_final/users_clean_final.csv
#         output_final/users_clean_final.json
#    - (Optional): use timestamps in the filename.
# 2. Call final_load_pipeline(df_hw_final, df_clean_final).
#
# YOUR CODE HERE


# BONUS EXERCISE 11 (OPTIONAL) - FILE GENERATION LOG
#
# OBJECTIVE:
# - Record which files your Load process generates.
#
# TASKS:
# 1. Create a function log_file_created(path) that:
#    - receives the path of a file
#    - opens (or creates) a file named "load_log.txt" in append mode
#    - writes a line containing:
#         TIMESTAMP,PATH
# 2. Modify one of your saving functions (for example:
#    save_all_formats or save_with_timestamp) so that it calls
#    log_file_created() after saving each file.
# 3. Inspect the contents of load_log.txt after several executions.
#
# YOUR CODE HERE


# END OF 03_LOAD - UNGUIDED EXERCISES
#
# If you complete these exercises:
# - You master the Load phase of a basic ETL.
# - You can save data in multiple formats.
# - You can control overwriting, versioning, and logging.
# - You are ready for 04_etl_projects to build complete ETL pipelines.

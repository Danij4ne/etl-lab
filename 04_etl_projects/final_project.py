
# FINAL_PROJECT.PY — PROFESSIONAL ETL PIPELINE
#
# Description:
# Complete ETL pipeline designed to simulate a real-world data
# engineering scenario. It combines several sources:
#   - Local CSV
#   - Local JSON
#   - Remote API
#
# It includes:
#   - Basic data validation
#   - Normalization
#   - Optional enrichment
#   - Final export layer
#
# This file defines the final structure. It does not contain solutions.


# 0. IMPORTS AND CONFIGURATION
#
# Tasks:
# 1. Import pandas as pd
# 2. Import requests
# 3. Import json
# 4. Import os
# 5. Import datetime
#
# 6. Define constant paths:
#       DATA_DIR
#       OUTPUT_DIR
#       CSV/JSON paths
#       Main API URL
#
# 7. (Optional): Define global logging variables
#
# YOUR CODE HERE


# 1. LOGGING (OPTIONAL)
#
# Objective:
# - Log the execution of the pipeline.
#
# Tasks:
# 1. Create a function log(message):
#       - Get a timestamp
#       - Create file etl_log.txt if it does not exist
#       - Write a line: TIMESTAMP, MESSAGE
#
# YOUR CODE HERE


# 2. BASIC VALIDATIONS
#
# Objective:
# - Detect data issues before transforming.
#
# Tasks:
# 1. Create a function validate_df(df, required_columns):
#       - Confirm that the required columns exist
#       - Confirm that the DataFrame is not empty
#       - If something fails → raise ValueError
#
# 2. (Optional) Type validation:
#       - Check if numeric columns are actually numeric
#       - Check if emails have a valid format
#
# YOUR CODE HERE


# 3. EXTRACT
#
# Objective:
# - Extract data from CSV, JSON, and API.
#
# Tasks:
# 3.1 extract_csv(path)
#       - Read CSV
#       - Validate minimum columns
#       - Return df
#
# 3.2 extract_json(path)
#       - Read JSON (with pandas or json.load)
#       - Validate minimum columns
#       - Return df
#
# 3.3 extract_api(url)
#       - Make a GET request
#       - Check status_code
#       - Extract list of users/objects
#       - Convert to DataFrame
#       - Validate structure
#
# 3.4 extract_all() → dict
#       - Call the three functions
#       - Return:
#           {
#             "csv": df_csv,
#             "json": df_json,
#             "api": df_api
#           }
#
# YOUR CODE HERE


# 4. TRANSFORM
#
# Objective:
# - Create a unified, clean, and normalized DataFrame.
#
# Tasks:
# 4.1 normalize_columns(df)
#       - Convert column names to lowercase
#       - Replace spaces with "_"
#
# 4.2 standardize_structures(data_sources: dict)
#       - Select relevant columns
#       - Rename columns for consistency
#       - Create a "source" column
#       - Return a list of DataFrames ready to combine
#
# 4.3 combine_sources(list_of_dfs)
#       - Concatenate
#       - Remove duplicates (by email or id)
#       - Reset index
#
# 4.4 enrich(df)
#       Optional:
#       - Create a full_name column
#       - Create an is_adult flag
#       - Convert date columns to datetime
#       - Clean null values
#
# 4.5 transform_all(data_dict)
#       - Full sequence:
#           normalize → standardize → combine → enrich
#       - Return df_final
#
# YOUR CODE HERE


# 5. LOAD
#
# Objective:
# - Save the output in multiple formats.
#
# Tasks:
# 5.1 ensure_output_dir()
#       - Create OUTPUT_DIR folder
#
# 5.2 save_csv(df, path)
#       - Save without index
#
# 5.3 save_json(df, path)
#       - orient="records"
#       - indent=2
#
# 5.4 load_all(df_final)
#       - Save:
#           OUTPUT_DIR/final_users.csv
#           OUTPUT_DIR/final_users.json
#       - Optional: export to Excel
#       - Optional: include timestamp in filenames
#
# YOUR CODE HERE


# 6. main() FUNCTION — OVERALL ORCHESTRATION
#
# Objective:
# - Chain all ETL pipeline phases.
#
# Tasks:
# main():
#   1. log("ETL started")
#   2. data = extract_all()
#   3. df_final = transform_all(data)
#   4. load_all(df_final)
#   5. log("ETL finished")
#
# Add:
# if __name__ == "__main__":
#       main()
#
# YOUR CODE HERE


# 7. FINAL (MANUAL) VALIDATION
#
# Tasks:
# - Display final shape
# - Display columns
# - Display first rows
# - Verify that the output files exist
#
# This part can go inside main() or separately.

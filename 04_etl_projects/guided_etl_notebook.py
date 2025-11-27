
# GUIDED_ETL_PIPELINE.PY
#
# Description:
# Example script for a complete ETL pipeline:
#   - Extract: CSV + JSON + API
#   - Transform: cleaning, normalization, combination
#   - Load: export to CSV and JSON
#
# This file is designed as a structured guide:
#   - It includes clear sections and functions to implement.
#   - It does not contain solutions.


# 0. IMPORTS AND BASIC CONFIGURATION
#
# Tasks:
# 1. Import:
#       - pandas as pd
#       - requests
#       - os
#       - json (optional)
#       - datetime (for timestamps or logs, optional)
# 2. Define path constants, for example:
#       DATA_DIR = "data"
#       OUTPUT_DIR = "output_final"
#       CSV_PATH = os.path.join(DATA_DIR, "users.csv")
#       JSON_PATH = os.path.join(DATA_DIR, "users_extra.json")
#
# YOUR CODE HERE


# 1. LOG FUNCTION (OPTIONAL BUT RECOMMENDED)
#
# Objective:
# - Log simple ETL events into a text file.
#
# Tasks:
# 1. Create a function log(message: str) that:
#       - Gets the current timestamp.
#       - Opens (or creates) a file "etl_log.txt" in append mode.
#       - Writes one line with: TIMESTAMP,MESSAGE
#
# Suggestion:
# - Use datetime.now().strftime(...) to format the date.
#
# YOUR CODE HERE


# 2. EXTRACT PHASE
#
# Objective:
# - Extract data from:
#       a) Local CSV
#       b) Local JSON
#       c) Remote API
#
# Recommended sources:
#   a) CSV:  data/users.csv
#   b) JSON: data/users_extra.json
#   c) API:  https://dummyjson.com/users?limit=10
#
# Tasks:
# 2.1 Create function extract_from_csv(path: str) -> pd.DataFrame
#       - Read CSV with pandas.
#       - Return a DataFrame.
#
# 2.2 Create function extract_from_json(path: str) -> pd.DataFrame
#       - Read JSON (with pandas or json + DataFrame).
#       - Return a DataFrame.
#
# 2.3 Create function extract_from_api(url: str) -> pd.DataFrame
#       - Make a GET request.
#       - Check status_code.
#       - Extract the list of users from the response.
#       - Convert it to a DataFrame.
#
# 2.4 Create function extract_all() -> dict[str, pd.DataFrame]
#       - Internally call:
#           df_csv = extract_from_csv(CSV_PATH)
#           df_json = extract_from_json(JSON_PATH)
#           df_api = extract_from_api(API_URL)
#       - Optional: call log() at each step.
#       - Return a dictionary, for example:
#           {
#             "csv": df_csv,
#             "json": df_json,
#             "api": df_api
#           }
#
# YOUR CODE HERE


# 3. TRANSFORM PHASE
#
# Objective:
# - Clean, normalize, and combine the extracted DataFrames.
#
# Considerations (example ideas, you decide how to apply them):
# - Normalize column names (lowercase, no spaces).
# - Ensure that key columns (id, email, name) are consistent.
# - Create a "source" column to identify the origin of each row.
# - Align structures between df_csv, df_json, and df_api before combining.
# - Remove duplicates by id or email, if it makes sense.
#
# Tasks:
# 3.1 Create function normalize_columns(df: pd.DataFrame) -> pd.DataFrame
#       - Normalize column names (for example: to lowercase).
#
# 3.2 Create function transform_data(data_dict: dict[str, pd.DataFrame]) -> pd.DataFrame
#       - Receives the dictionary returned by extract_all().
#       - Applies normalize_columns to each DataFrame.
#       - Selects relevant columns in each source.
#       - Adds a "source" column (for example: "csv", "json", "api").
#       - Combines the DataFrames (pd.concat).
#       - Removes duplicates if appropriate.
#       - Returns a final unified DataFrame.
#
# 3.3 (Optional) Create function additional_enrichment(df: pd.DataFrame) -> pd.DataFrame
#       - Examples:
#           * Create full_name from firstName + lastName.
#           * Create is_adult flag based on age.
#           * Normalize country into a standard format.
#
# YOUR CODE HERE


# 4. LOAD PHASE
#
# Objective:
# - Save the final DataFrame in output formats.
#
# Recommended formats:
#   - CSV
#   - JSON
#
# Tasks:
# 4.1 Create function ensure_output_dir(path: str) -> None
#       - Create folder if it does not exist (os.makedirs(path, exist_ok=True)).
#
# 4.2 Create function load_data(df: pd.DataFrame, basename: str) -> None
#       - Ensure OUTPUT_DIR exists.
#       - Save:
#           OUTPUT_DIR/basename + ".csv"
#           OUTPUT_DIR/basename + ".json"
#       - CSV without index.
#       - JSON with orient="records", indent=2.
#       - Optional: call log() to record generated paths.
#
# YOUR CODE HERE


# 5. main() FUNCTION — ETL ORCHESTRATION
#
# Objective:
# - Have a single entry point to run the pipeline.
#
# Tasks:
# 5.1 Create function main():
#       - Call log("ETL started") if you use logging.
#       - Call extract_all().
#       - Call transform_data(data_dict).
#       - (Optional) Call additional_enrichment(df_final).
#       - Call load_data(df_final, "etl_users_unified").
#       - Call log("ETL finished").
#
# 5.2 Add the standard execution block:
#       if __name__ == "__main__":
#           main()
#
# YOUR CODE HERE


# 6. BASIC VALIDATION (FOR MANUAL TESTS)
#
# Objective:
# - Make quick verification of the result easier.
#
# Ideas:
# - After running main(), you can:
#       - Print the number of records in the final DataFrame.
#       - Print the final columns.
#       - Load the generated CSV from disk and verify its shape.
#
# Note:
# - This part is optional and can be done inside main()
#   or in a small separate test block.

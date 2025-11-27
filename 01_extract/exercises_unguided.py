

# 01_EXTRACT - UNGUIDED EXERCISES

# Objective:
# - Practice the "E" part of ETL (Extract) WITHOUT step-by-step guidance.
# - Apply what you learned in the guided exercises.
# - Work with CSV, JSON, JSON Lines, multiple files, and APIs.
#
# Recommendation:
# - Try to solve each exercise WITHOUT looking at the previous ones.
# - If you get stuck, go back to the guided exercises.


# 0 IMPORTS

# TASK:
# - Import the necessary libraries for the exercises:
#   - pandas
#   - glob
#   - requests
#   - (optional) json
#

import pandas as pd 
import glob 
import requests 


# EXERCISE 1 - READ AND EXPLORE A CSV

# Use the file: data/simple_users.csv

# TASKS:
# 1. Load the CSV into a DataFrame called df_users.
# 2. Show:
#    - the first rows
#    - the number of rows and columns
#    - the column names
# 3. Check if there are null values in any column.
#

df_users = pd.read_csv("01_extract/data/simple_users.csv")

df_users.head()
df_users.shape
df_users.columns
df_users.isnull().sum()


# EXERCISE 2 - FILTER AND SORT DATA FROM THE CSV

# Using df_users from the previous exercise:

# TASKS:
# 1. Create a new DataFrame with only the columns:
#    - "name"
#    - "email"
# 2. Filter users whose name has more than 4 characters.
# 3. Sort the result by "name" in ascending order.

# 1. DataFrame with only name and email
df_columns = df_users[["name", "email"]]

# 2. Filter users with name length > 4
df_filtered = df_columns[df_columns["name"].str.len() > 4]

# 3. Sort by name ascending
df_filtered = df_filtered.sort_values(by="name", ascending=True)

print(df_filtered.head())


# EXERCISE 3 - READ A JSON AND COMPARE IT

# Use the file: data/simple_users.json

# TASKS:
# 1. Read the JSON into a DataFrame called df_users_json.
# 2. Compare the columns of df_users_json with those of df_users.
# 3. Write in a comment whether they have the same columns or not.

df_users_json = pd.read_json("01_extract/data/simple_users.json")

columnas_comunes = set(df_users.columns) & set(df_users_json.columns)
print("Columnas en común:", columnas_comunes)

mismas_columnas = set(df_users.columns) == set(df_users_json.columns)
print("¿Mismas columnas?:", mismas_columnas)


# EXERCISE 4 - READ JSON LINES

# Use the file: data/api_sample.jsonl

# TASKS:
# 1. Load the file into a DataFrame called df_api_sample.
# 2. Show:
#    - first rows
#    - shape
# 3. Check if there are null values in any column.

df_api_sample = pd.read_json("01_extract/data/api_sample.jsonl", lines=True)

df_api_sample.head()
df_api_sample.shape
df_api_sample.isnull().sum()


# EXERCISE 5 - FUNCTION TO READ CSV

# TASK:
# - Create a function named load_csv(path) that:
#   1. Receives a file path (path).
#   2. Tries to read the CSV into a DataFrame.
#   3. Returns the DataFrame.
#
# Extra (optional):
# - Add error handling with try/except and a friendly print
#   if the file does not exist.

def load_csv(path):
    try:
        file = pd.read_csv(path)
        return file 
    except:
        print("Ha ocurrido un error , vuelve a intentarlo")
        return None


# EXERCISE 6 - USING GLOB WITH A FUNCTION

# TASK:
# 1. Use glob to find all CSV files inside data/.
# 2. Create a function called load_all_csv_from_data() that:
#    - Receives no parameters.
#    - Searches for all CSVs in data/.
#    - Reads them one by one.
#    - Returns a single combined DataFrame.
#
# Note:
# - You can reuse load_csv() if you created it in exercise 5.

def load_all_csv_from_data():
    files = glob.glob("01_extract/data/*.csv")  # 1. Search CSVs
    dataframes = []                             # Empty list

    for file in files:                          # 2. Iterate one by one
        df = load_csv(file)                     # Read CSV
        if df is not None:                      # Avoid errors
            dataframes.append(df)               # Save DataFrame

    # 3. Combine all into a single DataFrame
    if dataframes:
        return pd.concat(dataframes, ignore_index=True)
    else:
        print("No CSV files found.")
        return None


# EXERCISE 7 - EXTRACTION FROM AN API

# API to use:
# - URL: https://dummyjson.com/users?limit=10

# TASKS:
# 1. Make a GET request to the API.
# 2. Convert the JSON response into a DataFrame called df_api_users.
# 3. Show:
#    - first rows
#    - shape
#    - columns

respond = requests.get("https://dummyjson.com/users?limit=10")

data = respond.json()          # Convert response to dictionary

df_api_users = pd.DataFrame(data["users"])   # Convert list to DataFrame

print(df_api_users.head())
print(df_api_users.shape)
print(df_api_users.columns)


# EXERCISE 8 - SELECT AND RENAME API COLUMNS

# Using df_api_users:

# TASKS:
# 1. Create a DataFrame named df_api_clean with the columns:
#    - "firstName"
#    - "lastName"
#    - "age"
#    - "email"
#    - "gender"
# 2. Rename columns to:
#    - "first_name"
#    - "last_name"
#    - "age"
#    - "email"
#    - "gender"

df_api_clean = df_api_users[["firstName", "lastName", "age", "email", "gender"]]

df_api_clean = df_api_clean.rename(columns={
    "firstName": "first_name",
    "lastName": "last_name"
})

print(df_api_clean.head())


# EXERCISE 9 - COMBINE DIFFERENT SOURCES

# Using:
# - df_users (CSV)
# - df_api_clean (API)

# TASKS:
# 1. Select a subset of columns from df_users that are comparable 
#    or similar to df_api_clean (for example: name, email).
# 2. Create a DataFrame called df_all_users where:
#    - you combine users from the CSV and the API
#    - columns have a format as similar as possible
# 3. Show the first rows of df_all_users.

# From CSV: use name and email
df_users_subset = df_users[["name", "email"]].copy()

# From API: create a similar "name" column from first_name + last_name
df_api_subset = df_api_clean[["first_name", "last_name", "email"]].copy()
df_api_subset["name"] = df_api_subset["first_name"] + " " + df_api_subset["last_name"]

# Keep same columns order as df_users_subset
df_api_subset = df_api_subset[["name", "email"]]

df_all_users = pd.concat([df_users_subset, df_api_subset], ignore_index=True)

print(df_all_users.head())

combined_data = {
    "csv_users": df_users_subset,
    "api_users": df_api_subset,
    "all_users": df_all_users
}


# EXERCISE 10 - CREATE YOUR OWN extract() FUNCTION

# OBJECTIVE:
# - Simulate the "E" part of an ETL.
#
# TASK:
# 1. Create a function named extract() that:
#    - Receives no parameters.
#    - Inside:
#       * reads the CSV (simple_users.csv)
#       * reads the JSON (simple_users.json)
#       * reads the JSONL (api_sample.jsonl)
#       * makes the API request (dummyjson, 10 users)
#    - Returns a dictionary named extracted_data with:
#       {
#         "csv": df_csv,
#         "json": df_json,
#         "jsonl": df_jsonl,
#         "api_users": df_api_users
#       }
# 2. Call extract() and save the result in a variable.
# 3. Print the dictionary keys and the shape of each DataFrame.

def extract():
    mcsv = pd.read_csv("01_extract/data/simple_users.csv")
    mjson = pd.read_json("01_extract/data/simple_users.json")
    mjsonl = pd.read_json("01_extract/data/api_sample.jsonl", lines=True)

    rq = requests.get("https://dummyjson.com/users?limit=10")
    rqj = rq.json()

    mrequest = pd.DataFrame(rqj["users"])

    extracted_data = {
        "csv": mcsv,
        "json": mjson,
        "jsonl": mjsonl,
        "api_users": mrequest
    }

    return extracted_data


extracted_data = extract()

# Print keys
for key in extracted_data.keys():
    print("Key:", key)

# Print shape of each DataFrame
for key, df in extracted_data.items():
    print(key, df.shape)


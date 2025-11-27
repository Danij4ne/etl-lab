
# 02_TRANSFORM 
#
# Objective:
# - Practice the "T" part of ETL (Transform) step by step.
# - Work with:
#     * Unit conversion (inches → meters, pounds → kilograms)
#     * Cleaning dirty data
#     * Text normalization
#     * Handling nulls and duplicates
#
# Reminder:
# - Here you have instructions and hints, but NO solutions.
# - The goal is understanding what you are doing, not copying.


#  IMPORTS
#
# TASK:
# 1. Import pandas as pd.
#
# HINT:
# import pandas as pd
#
# YOUR CODE HERE


#  EXERCISE 1 - LOAD heights_weights.csv
#
# File: data/heights_weights.csv
#
# Columns:
# - name
# - height_inch  (height in inches)
# - weight_lb    (weight in pounds)
#
# OBJECTIVES:
# - Load the CSV into a DataFrame.
# - View a sample of the data.
#
# STEPS:
# 1. Read the CSV into a DataFrame called df_hw.
# 2. Display the first rows using head().
# 3. Print df_hw.shape to see rows and columns.
# 4. Print df_hw.dtypes to check data types.
#
# HINT:
# df_hw = pd.read_csv("data/heights_weights.csv")


#  EXERCISE 2 - CONVERT UNITS (height and weight)
#
# OBJECTIVES:
# - Create new columns with metric units.
#
# DATA:
# - 1 inch = 0.0254 meters
# - 1 pound ≈ 0.45359237 kilograms
#
# STEPS:
# 1. Create a new column "height_m" from "height_inch".
# 2. Create a new column "weight_kg" from "weight_lb".
# 3. (Optional) round both columns to 2 decimals.
# 4. Display the first rows to verify the result.
#
# HINTS:
# df_hw["height_m"] = df_hw["height_inch"] * 0.0254
# df_hw["weight_kg"] = df_hw["weight_lb"] * 0.45359237
# df_hw.round(2) or use round() in each assignment
#
# YOUR CODE HERE


#   EXERCISE 3 - CREATE BMI COLUMN (Body Mass Index)
#
# Approximate formula:
# BMI = weight_kg / (height_m ^ 2)
#
# OBJECTIVE:
# - Add a "bmi" column to the DataFrame.
#
# STEPS:
# 1. Use the "weight_kg" and "height_m" columns to calculate BMI.
# 2. Store the result in a new column "bmi".
# 3. Round BMI to 2 decimals (optional).
# 4. Display the first rows.
#
# HINT:
# df_hw["bmi"] = df_hw["weight_kg"] / (df_hw["height_m"] ** 2)
#
# YOUR CODE HERE


#  EXERCISE 4 - LOAD dirty_data.csv
#
# File: data/dirty_data.csv
#
# Columns:
# - name     (may contain spaces and uppercase letters)
# - email    (may contain spaces, uppercase letters, and errors)
# - age      (may contain null values)
# - country  (may have variations: "spain", "Spain", " España", "SPAIN"...)
#
# OBJECTIVES:
# - Load the CSV.
# - Understand how "dirty" it is.
#
# STEPS:
# 1. Read the CSV into a DataFrame called df_dirty.
# 2. Display the first rows.
# 3. Print df_dirty.dtypes.
# 4. Print df_dirty.isna().sum() to inspect nulls.
#
# YOUR CODE HERE


#   EXERCISE 5 - CLEAN SPACES AND CASE FORMATTING
#
# OBJECTIVES:
# - Remove unnecessary spaces.
# - Normalize uppercase/lowercase usage.
#
# STEPS:
# 1. Clean the "name" column:
#    - Remove leading and trailing spaces.
#    - Capitalize the first letter and lowercase the rest (optional).
# 2. Clean the "email" column:
#    - Remove leading and trailing spaces.
#    - Convert everything to lowercase.
#
# HINTS:
# df_dirty["name"] = df_dirty["name"].str.strip()
# df_dirty["email"] = df_dirty["email"].str.strip().str.lower()
# To capitalize names: .str.capitalize() or .str.title()
#
# YOUR CODE HERE


#  EXERCISE 6 - NORMALIZE THE country COLUMN
#
# OBJECTIVE:
# - Ensure all "country" values represent the same thing with the same format.
#
# EXAMPLE VALUES:
# - "spain ", "Spain", "SPAIN", " España", "spain"
#
# STEPS:
# 1. Remove leading and trailing spaces.
# 2. Convert all values to lowercase.
# 3. Optional: replace all variations with a single normalized form ("Spain" or "spain").
#
# HINTS:
# df_dirty["country"] = df_dirty["country"].str.strip()
# df_dirty["country"] = df_dirty["country"].str.lower()
# df_dirty["country"] = df_dirty["country"].replace({"españa": "spain"})
#
# YOUR CODE HERE


#   EXERCISE 7 - HANDLE NULLS IN age
#
# OBJECTIVE:
# - Decide what to do with null values in the "age" column.
#
# OPTIONS:
# - Fill nulls with the mean.
# - Fill nulls with a fixed value (e.g., 0 or 18).
# - Drop rows with null age (less recommended generally, but valid depending on context).
#
# STEPS:
# 1. Check how many nulls exist in "age".
# 2. Choose a strategy and apply it.
# 3. Verify that "age" has no remaining nulls.
#
# HINTS:
# df_dirty["age"] = df_dirty["age"].fillna(df_dirty["age"].mean())
# or
# df_dirty = df_dirty.dropna(subset=["age"])
#
# YOUR CODE HERE


#   EXERCISE 8 - REMOVE DUPLICATES
#
# OBJECTIVE:
# - Remove duplicate rows from df_dirty.
#
# STEPS:
# 1. Check how many rows exist before removing duplicates.
# 2. Apply drop_duplicates().
# 3. Check how many rows remain afterward.
#
# HINTS:
# df_dirty.shape
# df_dirty = df_dirty.drop_duplicates()
#
# YOUR CODE HERE


#  EXERCISE 9 - CREATE A FINAL CLEAN DATAFRAME
#
# OBJECTIVE:
# - Obtain a "clean" and ready-to-use version of df_dirty.
#
# STEPS:
# 1. Choose which columns to keep (for example: name, email, age, country).
# 2. Create a new DataFrame called df_clean containing only these columns.
# 3. Review the first rows and the data types.
#
# HINT:
# df_clean = df_dirty[["name", "email", "age", "country"]]
#
# YOUR CODE HERE


#   EXERCISE 10 - CREATE A transform_data() FUNCTION
#
# OBJECTIVE:
# - Simulate the Transform function of an ETL process.
#
# TASK:
# 1. Create a function called transform_data() that:
#    - Takes no parameters (for now).
#    - Inside the function:
#        * reads heights_weights.csv
#        * performs metric conversions
#        * calculates BMI
#        * reads dirty_data.csv
#        * cleans names, emails, country, nulls, and duplicates
#    - Returns:
#        * df_hw transformed
#        * df_clean (clean version of dirty_data)
# 2. Call transform_data() and store the result in two variables.
# 3. Print:
#    - the head() of both DataFrames
#    - the shape of each one
#
# SUGGESTED INTERFACE:
# def transform_data():
#     ...
#     return df_hw, df_clean
#
 



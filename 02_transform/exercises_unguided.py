
# 02_TRANSFORM - UNGUIDED EXERCISES
#
# Objective:
# - Practice Transform (the "T" in ETL) on your own, without direct guidance.
# - Apply what you learned about unit conversion, data cleaning, normalization,
#   handling nulls, removing duplicates, and creating new columns.
#
# Recommendation:
# - Try each exercise WITHOUT looking at the guided version.
# - If you get stuck, go back to the guided exercises to refresh ideas.


# 0️⃣ IMPORTS
#
# IMPORTANT:
# - Import pandas as pd.
# - Load the datasets when needed.
#
# YOUR CODE HERE


# 1️⃣ EXERCISE 1 - CONVERT UNITS IN heights_weights.csv
#
# File: data/heights_weights.csv
#
# TASKS:
# 1. Load the CSV into a DataFrame called df_hw.
# 2. Create the columns:
#    - "height_m" (meters)
#    - "weight_kg" (kilograms)
# 3. Round both columns to 2 decimals.
# 4. Display:
#    - the first rows
#    - df_hw.describe()
#
# NOTE:
# - No hints here: you already did this in the guided exercises.
#
# YOUR CODE HERE


# 2️⃣ EXERCISE 2 - CALCULATE BMI
#
# TASKS:
# 1. Using df_hw from the previous exercise:
#    - create a "bmi" column
#      BMI = weight_kg / (height_m ** 2)
# 2. Round to 2 decimals.
# 3. Display the first rows.
#
# YOUR CODE HERE


# 3️⃣ EXERCISE 3 - LOAD AND ANALYZE dirty_data.csv
#
# File: data/dirty_data.csv
#
# TASKS:
# 1. Load the DataFrame df_dirty.
# 2. Inspect:
#    - head()
#    - shape
#    - dtypes
#    - nulls per column
#    - duplicated rows
#
# YOUR CODE HERE


# 4️⃣ EXERCISE 4 - CLEAN SPACES AND CASE FORMATTING
#
# TASKS:
# 1. Clean "name":
#    - remove spaces
#    - normalize to name format (e.g., Ana, Carlos)
# 2. Clean "email":
#    - remove spaces
#    - convert to lowercase
#
# OBJECTIVE:
# - Make name and email consistent and clean.
#
# YOUR CODE HERE


# 5️⃣ EXERCISE 5 - NORMALIZE THE country COLUMN
#
# TASKS:
# 1. Remove extra spaces.
# 2. Convert everything to lowercase.
# 3. Normalize all variants to one single value:
#    - "spain", "Spain", " España", "SPAIN", etc.
#
# SUGGESTION:
# - Choose the final format yourself (for example: "spain").
#
# YOUR CODE HERE


# 6️⃣ EXERCISE 6 - HANDLE NULLS IN age
#
# TASKS:
# 1. Analyze how many nulls exist.
# 2. Choose a strategy:
#    - fill with mean
#    - fill with median
#    - fill with a constant
#    - drop rows with nulls
# 3. Apply the strategy.
# 4. Verify that there are no nulls left.
#
# YOUR CODE HERE


# 7️⃣ EXERCISE 7 - REMOVE DUPLICATES
#
# TASKS:
# 1. Check how many rows exist before cleaning.
# 2. Remove duplicates.
# 3. Check how many rows remain afterwards.
# 4. Ensure df_dirty has no duplicates.
#
# YOUR CODE HERE


# 8️⃣ EXERCISE 8 - CREATE A FINAL CLEAN DATAFRAME
#
# TASKS:
# 1. Select only the clean columns you want:
#    - name
#    - email
#    - age
#    - country
# 2. Create a DataFrame df_clean with these columns.
# 3. Print:
#    - head()
#    - shape
#    - dtypes
#
# OBJECTIVE:
# - Have df_clean ready for the Load phase.
#
# YOUR CODE HERE


# 9️⃣ EXERCISE 9 - JOIN df_hw (converted) WITH df_clean (clean)
#
# OBJECTIVE:
# - Practice joins between transformed datasets.
#
# TASKS:
# 1. Ensure df_hw and df_clean have a common column.
# 2. Perform a merge or join between both DataFrames.
# 3. Choose the join type (inner, left, etc.).
# 4. Display the result.
#
# NOTE:
# - If you do not have a common column, create one:
#   For example: convert names to lowercase in both DataFrames.
#
# YOUR CODE HERE


# 🔟 EXERCISE 10 - CREATE A transform() FUNCTION
#
# OBJECTIVE:
# - Simulate a real Transform module in a professional ETL workflow.
#
# TASK:
# 1. Create a function transform() that:
#    - reads heights_weights.csv
#    - performs conversions (m, kg, bmi)
#    - reads dirty_data.csv
#    - cleans name, email, country, age
#    - removes duplicates
#    - creates df_hw_final and df_clean_final
# 2. Return both DataFrames.
# 3. Verify their shapes and first rows.
#
# SUGGESTED INTERFACE:
# def transform():
#     ...
#     return df_hw_final, df_clean_final
#
# YOUR CODE HERE



# 🎯 BONUS EXERCISE 11 (OPTIONAL)
#
# OBJECTIVE:
# - Take Transform to the next level.
#
# TASKS:
# 1. Create a function clean_email(email) that:
#    - removes spaces
#    - converts to lowercase
#    - validates that the email contains exactly 1 "@"
#    - returns None if invalid
# 2. Apply it to the entire email column.
#
# EXTRA CHALLENGE:
# - Count how many invalid emails were detected.
#
# YOUR CODE HERE







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


# IMPORTS
#
# IMPORTANT:
# - Import pandas as pd.
# - Load the datasets when needed.
#

import pandas as pd


# EXERCISE 1 - CONVERT UNITS IN heights_weights.csv
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

df_hw = pd.read_csv("02_transform/data/heights_weights.csv")
print(df_hw)

df_hw["height_m"] = round(df_hw["height_inch"] * 0.0254 , 2)
df_hw["weight_kg"] = round(df_hw["weight_lb"] * 0.453592 , 2)

print(df_hw.head())

print(df_hw.describe())

# EXERCISE 2 - CALCULATE BMI
#
# TASKS:
# 1. Using df_hw from the previous exercise:
#    - create a "bmi" column
#      BMI = weight_kg / (height_m ** 2)
# 2. Round to 2 decimals.
# 3. Display the first rows.
#

df_hw["BMI"] = round(df_hw["weight_kg"] / (df_hw["height_m"] **2), 2)
print(df_hw)


# EXERCISE 3 - LOAD AND ANALYZE dirty_data.csv
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

df_dirty = pd.read_csv("02_transform/data/dirty_data.csv") 
print(df_dirty)
print(df_dirty.head(2))
print(df_dirty.shape)
print(df_dirty.dtypes)

print(df_dirty.isnull().sum())

print(df_dirty[df_dirty.duplicated()])

# EXERCISE 4 - CLEAN SPACES AND CASE FORMATTING
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
 
df_dirty["name"] =  df_dirty["name"].str.strip().str.title()
df_dirty["email"] =  df_dirty["email"].str.strip().str.lower()

# EXERCISE 5 - NORMALIZE THE country COLUMN
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
 
df_dirty["country"] = df_dirty["country"].str.strip().str.lower()
df_dirty["country"] = df_dirty["country"].replace({"españa": "spain"})


# EXERCISE 6 - HANDLE NULLS IN age
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
 
print(df_dirty["age"].isna().sum())

median_age = df_dirty["age"].median()

df_dirty["age"] = df_dirty["age"].fillna(median_age)

print(df_dirty["age"].isna().sum())



# EXERCISE 7 - REMOVE DUPLICATES
#
# TASKS:
# 1. Check how many rows exist before cleaning.
# 2. Remove duplicates.
# 3. Check how many rows remain afterwards.
# 4. Ensure df_dirty has no duplicates.
#
 
 
print("Rows before cleaning:", df_dirty.shape)

 
print("Duplicate rows before cleaning:")
print(df_dirty[df_dirty.duplicated()])  

 
df_dirty = df_dirty.drop_duplicates()
 

print("Rows after cleaning:", df_dirty.shape)

 
print("Remaining duplicates:", df_dirty.duplicated().sum())



# EXERCISE 8 - CREATE A FINAL CLEAN DATAFRAME
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
 

print(df_dirty)

df_clean = df_dirty[["name","email","age","country"]]

print(df_clean.head())

print(df_clean.shape)

print(df_clean.dtypes)



#  EXERCISE 9 - JOIN df_hw (converted) WITH df_clean (clean)
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


df_final = pd.merge(df_clean, df_hw, on= "name" , how = "inner")
 


#  EXERCISE 10 - CREATE A transform() FUNCTION
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
 
def transform():
    ddf_h = pd.read_csv("02_transform/data/heights_weights.csv")
    ddf_h["m"] = round(ddf_h["height_inch"] * 0.0254 , 2)
    ddf_h["kg"] = round(ddf_h["weight_lb"] * 0.453592 , 2)
    ddf_h["BMI"] = round(ddf_h["kg"] / (ddf_h["m"] ** 2), 2)

    ddf_d = pd.read_csv("02_transform/data/dirty_data.csv")
    ddf_d["name"] = ddf_d["name"].str.strip().str.title()
    ddf_d["email"] = ddf_d["email"].str.strip().str.lower()

    m_age = ddf_d["age"].mean()
    ddf_d["age"] = ddf_d["age"].fillna(m_age)

    ddf_d["country"] = ddf_d["country"].str.replace("España", "Spain")
    ddf_d["country"] = ddf_d["country"].str.strip().str.title()

    ddf_d.drop_duplicates(inplace=True)

    return ddf_h, ddf_d

df_hw_final, df_clean_final = transform()

print(df_clean_final.head())
print(df_clean_final.shape)

print(df_hw_final.head())
print(df_hw_final.shape)





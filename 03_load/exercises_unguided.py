
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

import pandas as pd
import os 


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
 

df = pd.read_csv("03_load/data/sample_to_save.csv")
print(df)
print(df.head(2))
print(df.shape)
print(df.dtypes)



# 2 EXERCISE 2 - CREATE OUTPUT FOLDER
#
# TASKS:
# 1. Create a folder named "output" if it does not exist.
# 2. Check in your terminal or file explorer that it was created.
#
# NOTE:
# - Use the same "output" folder for all following exercises.
#
 

os.makedirs("output", exist_ok= True)


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

df.to_csv("output/data_semicolon.csv", sep=";" , index = False)


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


df.to_json("output/data_by_columns.json" , orient= "columns" )


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

df_small = df[["name","email"]]

df_small.to_csv("output/data_contacts.csv" , index= False)



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
 
df.to_excel("output/data_users.xlsx", sheet_name="Users", index=False)


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

 

def save_all_formats(df, basename):
    os.makedirs("output" , exist_ok= True)
    df.to_csv(f"output/{basename}.csv" , index= False)
    df.to_json(f"output/{basename}.json" , orient = "records" , indent = 2 )
    df.to_excel(f"output/{basename}.xlsx" ,index = False )

save_all_formats(df, "users_full")



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

 

def save_if_not_exists(df, path):
    if not os.path.exists(path):               
        df.to_csv(path, index=False)           
        print("File saved successfully.")
    else:
        print("The file already exists. It has not been overwritten.")

save_if_not_exists(df, "output/users_safe.csv")
save_if_not_exists(df, "output/users_safe.csv")




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
 
from datetime import datetime
 

def save_with_timestamp(df, base_name):
    os.makedirs("output", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"output/{base_name}_{timestamp}.csv"

    df.to_csv(filename, index=False)

    print(f"File saved as: {filename}")

save_with_timestamp(df, "users_version")
save_with_timestamp(df, "users_version")




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


def final_load_pipeline(df_hw_final, df_clean_final):
     
    os.makedirs("output_final", exist_ok=True)
    
    df_hw_final.to_csv("output_final/heights_weights_final.csv", index=False)
    
    df_clean_final.to_csv("output_final/users_clean_final.csv", index=False)
    
    df_clean_final.to_json(
        "output_final/users_clean_final.json",
        orient="records",
        indent=2
    )

df_hw_final = df.copy()
df_clean_final = df.copy()

final_load_pipeline(df_hw_final, df_clean_final)



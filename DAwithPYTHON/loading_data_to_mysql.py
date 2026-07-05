
# engine = create_engine("mysql+mysqlconnector://root:Bharath%4001@localhost:3306/Naukri_jobs")

import pandas as pd
import numpy as np

# Load your file
df = pd.read_csv("FINAL_CLEAN_DATASET.csv")

# Generate the SQL file
with open("data_import.sql", "w", encoding="utf-8") as f:
    f.write("USE Naukri_jobs;\n")
    for _, row in df.iterrows():
        # Function to clean values for SQL
        def clean(val):
            # If it's NaN/None, return the word NULL without quotes
            if pd.isna(val) or val is None:
                return "NULL"
            # If it's a number, return  as a string
            if isinstance(val, (int, float)):
                return str(val)
            # If it's a string, escape quotes and in single quotes
            return f"'{str(val).replace("'", "''")}'"

        #the insert row
        query = (f"INSERT INTO job_data (Title, Company, Location, Skills, min_exp, max_exp, min_sal, max_sal) "
                 f"VALUES ({clean(row['Title'])}, {clean(row['Company'])}, {clean(row['Location'])}, "
                 f"{clean(row['Skills'])}, {clean(row['min_exp'])}, {clean(row['max_exp'])}, "
                 f"{clean(row['min_sal'])}, {clean(row['max_sal'])});\n")
        f.write(query)

print("SUCCESS: File 'data_import.sql' created in your project folder.")

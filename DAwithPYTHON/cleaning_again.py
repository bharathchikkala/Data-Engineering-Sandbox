import pandas as pd
import numpy as np
import re
import csv


df = pd.read_csv("CAREER_MASTER_DATASET.csv")


def parse_salary(salary_str):
    s = str(salary_str).lower().replace(',', '').strip()
    # Handle not disclosed
    if pd.isna(salary_str) or any(x in s for x in ['not', 'disclosed', 'unpaid', 'nan']):
        return np.nan, np.nan

    # get numbers
    nums = [float(n) for n in re.findall(r"\d+\.?\d*", s)]
    if not nums: return np.nan, np.nan

    # unit multiplier
    multiplier = 100000 if 'l' in s else 1000 if 'k' in s else 1

    # Adjust for monthly
    if 'month' in s or '/mo' in s:
        nums = [n * 12 for n in nums]

    # Apply multiplier
    nums = [n * multiplier for n in nums]

    # Return sorted (min, max)
    return min(nums), max(nums)


# experience
def parse_exp(exp_str):
    exp_str = str(exp_str).lower()
    if 'not' in exp_str or 'unpaid' in exp_str or pd.isna(exp_str):
        return np.nan, np.nan
    nums = [int(n) for n in re.findall(r'\d+', exp_str)]
    return (min(nums), max(nums)) if nums else (np.nan, np.nan)



sal_data = df['Salary'].apply(parse_salary)
df['min_sal'], df['max_sal'] = zip(*sal_data)

exp_data = df['Experience'].apply(parse_exp)
df['min_exp'], df['max_exp'] = zip(*exp_data)

# saving
df.to_csv("FINAL_CLEAN_DATASET.csv", index=False, quoting=csv.QUOTE_ALL)
print("SUCCESS: FINAL_CLEAN_DATASET.csv created.")

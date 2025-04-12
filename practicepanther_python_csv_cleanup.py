import pandas as pd
import random

# Legend for "Assigned" Column
assigned_map = {
    "GM": "Gabe Michel",
    "AA": "Aaron Artsen",
    "BL": "Bond Liver",
    "IC": "Individual Contributor",
    "TM": "Tim Mint"
}

# Load the .csv
df = pd.read_csv(r'Downloads\Migration_Interview_Data (Python) - Migration_Interview_Data.csv')

# 1. Remove Duplicate Rows
df = df.drop_duplicates()

# 2. Modify Column Headers - Prefix with "Contact: "
df.columns = ['Contact: ' + col for col in df.columns]

# 3. Standardize Name Formatting
df['Contact: First Name'] = df['Contact: First Name'].str.title()
df['Contact: Last Name'] = df['Contact: Last Name'].str.title()

# 4. Reformat Dates - Change "Date of Birth" from DD/MM/YYYY to MM/DD/YYYY
df['Contact: Date of Birth'] = pd.to_datetime(df['Contact: Date of Birth'], format='%d/%m/%Y').dt.strftime('%m/%d/%Y')

# 5. Generate Unique IDs
df['Contact: ID'] = [random.randint(1, 1000000) for _ in range(len(df))]

# if we wanted to have standard contact IDs in ascending order, that'd either be handled by the db import or alternatively we could do something like this df['Contact: ID'] = range(40000, 40000 + len(df)) (I think)

# 6. Adjust the "Assigned" Column - Replace initials with full names
df['Contact: Assigned'] = df['Contact: Assigned'].apply(lambda x: assigned_map.get(x, 'Gabe Michel'))

# 7. Save the transformed data to a new CSV file
df.to_csv(r'Downloads\Migration_Interview_Date (Python) - Migration_Interview_Data_Cleaned.csv', index=False)

print("Data transformation complete. Output saved to 'Migration_Interview_Date (Python) - Migration_Interview_Data_Cleaned.csv'.")



import pandas as pd
import json
import random

# Load Excel data
df = pd.read_excel('Accountpayload.xlsx')

# Convert to JSON
json_data = []
for index, row in df.iterrows():
    # print(row)
    # nullData = 'null'

    data = {
    "accountHolderName": row['accountHolderName'] ,
    "accountNum":  str(random.randint(100000000000, 999999999999)),
    "accountType": 'COMPANY',
    "emailId": "ig@gaiansolutions.com"
}
    json_data.append(data)

# Write JSON data to a file
output_filename = 'account.json'
with open(output_filename, 'w') as json_file:
    json.dump(json_data, json_file, indent=4)

print(f"JSON data has been written to '{output_filename}'")

# Add 'json' column to DataFrame
df['json'] = json_data

# Write updated DataFrame back to the same Excel file
df.to_excel('Accountpayload.xlsx', index=False)

print("JSON data has been added to the 'json' column in 'Accountpayload.xlsx'")
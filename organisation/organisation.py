import pandas as pd
import json
import random

# Load Excel data
df = pd.read_excel('orgPayload.xlsx')

# # Convert to JSON
json_data = []
for index, row in df.iterrows():
    # print(row)
    # nullData = 'null'

    data = {
    "registrationNumber": str(random.randint(1000000000, 9999999999)),
    "organisationName": row['organisationName'],
    "accountId": row['accountId'],
    "website": "www."+ str(row['organisationName']).replace(" ", "").replace(".", "")+".com",
    "routingNum": "4520005"

}
    json_data.append(data)

# Write JSON data to a file
output_filename = 'org.json'
with open(output_filename, 'w') as json_file:
    json.dump(json_data, json_file, indent=4)

print(f"JSON data has been written to '{output_filename}'")


# Add 'json' column to DataFrame
df['json'] = json_data

# Write updated DataFrame back to the same Excel file
df.to_excel('orgPayload.xlsx', index=False)

print("JSON data has been added to the 'json' column in 'Accountpayload.xlsx'")
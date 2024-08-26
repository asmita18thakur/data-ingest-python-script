import pandas as pd
import json
import random

# Load Excel data
df = pd.read_excel('otpPayload.xlsx')

# Convert to JSON
json_data = []
for index, row in df.iterrows():
    # print(row)
    # nullData = 'null'

    data = {
    "email": str(row['emailPrefix']).replace(" ", "").replace(".", "")+'@gatestautomation.com',
    "otp": "12345",
    "userType": "TENANT"
}
    json_data.append(data)

# Write JSON data to a file
output_filename = 'otp.json'
with open(output_filename, 'w') as json_file:
    json.dump(json_data, json_file, indent=4)

print(f"JSON data has been written to '{output_filename}'")
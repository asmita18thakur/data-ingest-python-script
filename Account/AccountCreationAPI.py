import json
import requests
import pandas as pd

# Load payloads from account.json
with open('account.json', 'r') as json_file:
    payloads = json.load(json_file)

# Load Excel data
df = pd.read_excel('Accountpayload.xlsx')

# API endpoint
url = 'https://ig.aidtaas.com/market-place/v1.0/accounts'

# Authorization token
token = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImZmOGYxNjhm...'

# Headers including Authorization token
headers = {
    'Content-Type': 'application/json',
    'Authorization': token
}

# List to store responses and Account IDs
responses = []
account_ids = []

# Iterate over each payload
for payload in payloads:
    # Make POST request
    response = requests.post(url, json=payload, headers=headers)
    
    # Handle the response
    if response.status_code == 201:  # Resource created successfully
        response_data = response.json()
        responses.append(response_data)
        account_ids.append(response_data['id'])
    else:
        responses.append(response.text)
        account_ids.append(response.text)
        print(f"Failed to create account: {response.text}")

# Save responses to a file
with open('Accountresponses.json', 'w') as responses_file:
    json.dump(responses, responses_file, indent=4)

print("Responses saved successfully.")

# Add 'AccountID' column to DataFrame
df['AccountID'] = account_ids

# Write updated DataFrame back to the same Excel file
df.to_excel('Accountpayload.xlsx', index=False)

print("Excel file updated with AccountIDs.")

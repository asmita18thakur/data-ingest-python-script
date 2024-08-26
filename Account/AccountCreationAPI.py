import json
import requests
import pandas as pd

# Load payloads from account.json
with open('account.json', 'r') as json_file:
    payloads = json.load(json_file)

# Load Excel data
df = pd.read_excel('Accountpayload.xlsx')

# API endpoint
url = 'https://ig.gov-cloud.ai/hcy-web/v1.0/accounts'

# Authorization token
token = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImZmOGYxNjhmLTNmZjYtNDZlMi1iMTJlLWE2YTdlN2Y2YTY5MCJ9.eyJwcm9maWxlVXJsIjoiaHR0cDovL2luZ3Jlc3MtZ2F0ZXdheS5nYWlhbnNvbHV0aW9ucy5jb20vY29udGVudC1zZXJ2aWNlL3YxLjAvY29udGVudC8xOTAxNjc4MS0zOGJmLTRhMzQtYTU0ZS03NjdkYjk2OGFhMDciLCJyZWNlbnRfc2Vzc2lvbiI6Ik5BIiwic3ViIjoiZ2FpYW4uY29tIiwicGFyZW50VGVuYW50SWQiOiJOQSIsImNvbG9yIjoiQmxhY2siLCJ1c2VyX25hbWUiOiJQcmFzYW5uYWt1bWFyIiwiaXNzIjoiZ2FpYW4uY29tIiwiaXNBZG1pbiI6dHJ1ZSwicGxhdGZvcm1JZCI6IjYwNDc4OWViNDJiN2RjMDAwMTdhODM0MSIsInVzZXJOYW1lIjoiUHJhc2FubmFrdW1hciIsImF1dGhvcml0aWVzIjpbIlJPTEVfTUFSS0VUUExBQ0VfVVNFUiJdLCJjbGllbnRfaWQiOiJnYWlhbiIsInNjb3BlIjpbInRydXN0IiwicmVhZCIsIndyaXRlIl0sInRlbmFudElkIjoiNjE1ZThiNTM5N2I5NGQwMDAxNTU0NDhjIiwibG9nbyI6Imh0dHA6Ly9pbmdyZXNzLWdhdGV3YXkuZ2FpYW5zb2x1dGlvbnMuY29tL2NvbnRlbnQtc2VydmljZS92MS4wL2NvbnRlbnQvMTkwMTY3ODEtMzhiZi00YTM0LWE1NGUtNzY3ZGI5NjhhYTA3IiwiZXhwIjoxNjkwNDIyNTUwLCJqdGkiOiJjOGUxOGRhMi0xYWM2LTQ5Y2YtYmVmNS1kMTJkNjNkZGViZWIiLCJlbWFpbCI6InByYXNhbm5ha3VtYXIubmFsYW1AZ2FpYW5zb2x1dGlvbnMuY29tIn0.ZNEq27R6YPjU-cQ9NqhVbX9CqcPYHQMYTnuVuOsELwuY83FqUBTsTR9d9RjZuqdfeKm6Ak9gIOB0fPzFYSLVw2T8PfqwWfmWS78oaqdGnDKaBGbGwUxditsk6fdm26xwjJbn7fkaPZ4bD8CZJVLvfM7jBj_mbSc5JOdYesEIDeb30HtTf1Cl7LZlm7cM1PTEpq66gCYjlfHCDeYYsnYEjDh5v0IbBsXY2UZPShL_xyv1cDhL0jlUQnZQ8x44RtremQ572SKh4jXeteQqMiIkZtgUFsFxXNCOuC5n1SQYG7RJ_rFsGJx1um55m4BeBg9Clf-Z_oJLgxzpWIt3_BsVBw'

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
# df['AccountID'] = account_ids

# Write updated DataFrame back to the same Excel file
df.to_excel('Accountpayload.xlsx', index=False)

print("Excel file updated with AccountIDs.")

import json
import requests
import pandas as pd
import uuid

# Token and headers setup
token = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImZmOGYxNjhmLTNmZjYtNDZlMi1iMTJlLWE2YTdlN2Y2YTY5MCJ9.eyJwcm9maWxlVXJsIjoiaHR0cDovL2luZ3Jlc3MtZ2F0ZXdheS5nYWlhbnNvbHV0aW9ucy5jb20vY29udGVudC1zZXJ2aWNlL3YxLjAvY29udGVudC8xOTAxNjc4MS0zOGJmLTRhMzQtYTU0ZS03NjdkYjk2OGFhMDciLCJyZWNlbnRfc2Vzc2lvbiI6Ik5BIiwic3ViIjoiZ2FpYW4uY29tIiwicGFyZW50VGVuYW50SWQiOiJOQSIsImNvbG9yIjoiQmxhY2siLCJ1c2VyX25hbWUiOiJQcmFzYW5uYWt1bWFyIiwiaXNzIjoiZ2FpYW4uY29tIiwiaXNBZG1pbiI6dHJ1ZSwicGxhdGZvcm1JZCI6IjYwNDc4OWViNDJiN2RjMDAwMTdhODM0MSIsInVzZXJOYW1lIjoiUHJhc2FubmFrdW1hciIsImF1dGhvcml0aWVzIjpbIlJPTEVfTUFSS0VUUExBQ0VfVVNFUiJdLCJjbGllbnRfaWQiOiJnYWlhbiIsInNjb3BlIjpbInRydXN0IiwicmVhZCIsIndyaXRlIl0sInRlbmFudElkIjoiNjE1ZThiNTM5N2I5NGQwMDAxNTU0NDhjIiwibG9nbyI6Imh0dHA6Ly9pbmdyZXNzLWdhdGV3YXkuZ2FpYW5zb2x1dGlvbnMuY29tL2NvbnRlbnQtc2VydmljZS92MS4wL2NvbnRlbnQvMTkwMTY3ODEtMzhiZi00YTM0LWE1NGUtNzY3ZGI5NjhhYTA3IiwiZXhwIjoxNjkwMzkwMjMzLCJqdGkiOiI4ZGEzZGQ2NS05ZTAxLTQ0YzMtYWUxZS1iYzk2NGZhMDkyMWQiLCJlbWFpbCI6InByYXNhbm5ha3VtYXIubmFsYW1AZ2FpYW5zb2x1dGlvbnMuY29tIn0.VYQOKYmCvIY8G0mJT0bu41VMddsV2aOkymfOx6LyTcfsMOX4RH1xjrpxnOltROYsfKw0dUhd-vP3N3CteV_P9gEjvsEb__BFQQz74naGOJnoCZNxuTu-orzaEfG42Ki0xBb833Xp65TC0fI815sD-CP56RAKYtMArpnAp3QbvFHJ6lQUhXQo6h6HhU0itn1k3Ttr6_hhok4Yl6NYIib3oJ7VY27h2Z21-fr4hVza1qyFE29edjr-ElAxPxVahbREYaB9uKJp2NZaGobJDCmgYcEhvGGGdOimx8h5oW-3P1BFG6d0Y0lMmB2IVnZ5tgbCOGvivfJzf-t8_ndvQxB-Zg'
headers = {
    'Content-Type': 'application/json',
    'Authorization': token
}

# Load the initial payloads and Excel data
with open('org.json', 'r') as json_file:
    payloads = json.load(json_file)

# Initialize an empty DataFrame to store detailed response data
columns = ['OrgID', 'Status', 'Detail']  # Customize these columns based on the specific data you need
df_responses = pd.DataFrame(columns=columns)

# API endpoint
url = 'https://ig.gov-cloud.ai/hcy-web/v1.0/organisations'

# Lists to store response data and unique IDs
responses = []
org_ids = []

# Process each payload
for payload in payloads:
    transaction_id = str(uuid.uuid4())
    response = requests.post(url, json=payload, headers=headers)
    
    # Prepare data row for DataFrame
    if response.status_code in [200, 201]:
        response_data = response.json()
        row = {
            'OrgID': response_data.get('id', 'No ID returned'),
            'Status': 'Success',
            'Detail': json.dumps(response_data)  # Storing the whole response as a JSON string
        }
    else:
        row = {
            'OrgID': 'Error',
            'Status': f'Failed with status {response.status_code}',
            'Detail': response.text  # Store error message
        }
    
    # Append row to the DataFrame
    df_responses = df_responses._append(row, ignore_index=True)


# Save the DataFrame to an Excel file
df_responses.to_excel('Org_response.xlsx', index=False)


# Convert DataFrame to a list of dicts and save to JSON file
response_json_data = df_responses.to_dict(orient='records')
with open('OrgResponses.json', 'w') as responses_file:
    json.dump(response_json_data, responses_file, indent=4)

print("Responses saved successfully.")

print("Data processing complete. Check 'Org_response.xlsx' and 'OrgResponses.json' for results.")

import json
import requests
import pandas as pd

token = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImZmOGYxNjhmLTNmZjYtNDZlMi1iMTJlLWE2YTdlN2Y2YTY5MCJ9.eyJwcm9maWxlVXJsIjoiaHR0cDovL2luZ3Jlc3MtZ2F0ZXdheS5nYWlhbnNvbHV0aW9ucy5jb20vY29udGVudC1zZXJ2aWNlL3YxLjAvY29udGVudC8xOTAxNjc4MS0zOGJmLTRhMzQtYTU0ZS03NjdkYjk2OGFhMDciLCJyZWNlbnRfc2Vzc2lvbiI6Ik5BIiwic3ViIjoiZ2FpYW4uY29tIiwicGFyZW50VGVuYW50SWQiOiJOQSIsImNvbG9yIjoiQmxhY2siLCJ1c2VyX25hbWUiOiJQcmFzYW5uYWt1bWFyIiwiaXNzIjoiZ2FpYW4uY29tIiwiaXNBZG1pbiI6dHJ1ZSwicGxhdGZvcm1JZCI6IjYwNDc4OWViNDJiN2RjMDAwMTdhODM0MSIsInVzZXJOYW1lIjoiUHJhc2FubmFrdW1hciIsImF1dGhvcml0aWVzIjpbIlJPTEVfTUFSS0VUUExBQ0VfVVNFUiJdLCJjbGllbnRfaWQiOiJnYWlhbiIsInNjb3BlIjpbInRydXN0IiwicmVhZCIsIndyaXRlIl0sInRlbmFudElkIjoiNjE1ZThiNTM5N2I5NGQwMDAxNTU0NDhjIiwibG9nbyI6Imh0dHA6Ly9pbmdyZXNzLWdhdGV3YXkuZ2FpYW5zb2x1dGlvbnMuY29tL2NvbnRlbnQtc2VydmljZS92MS4wL2NvbnRlbnQvMTkwMTY3ODEtMzhiZi00YTM0LWE1NGUtNzY3ZGI5NjhhYTA3IiwiZXhwIjoxNjkwMzkwMjMzLCJqdGkiOiI4ZGEzZGQ2NS05ZTAxLTQ0YzMtYWUxZS1iYzk2NGZhMDkyMWQiLCJlbWFpbCI6InByYXNhbm5ha3VtYXIubmFsYW1AZ2FpYW5zb2x1dGlvbnMuY29tIn0.VYQOKYmCvIY8G0mJT0bu41VMddsV2aOkymfOx6LyTcfsMOX4RH1xjrpxnOltROYsfKw0dUhd-vP3N3CteV_P9gEjvsEb__BFQQz74naGOJnoCZNxuTu-orzaEfG42Ki0xBb833Xp65TC0fI815sD-CP56RAKYtMArpnAp3QbvFHJ6lQUhXQo6h6HhU0itn1k3Ttr6_hhok4Yl6NYIib3oJ7VY27h2Z21-fr4hVza1qyFE29edjr-ElAxPxVahbREYaB9uKJp2NZaGobJDCmgYcEhvGGGdOimx8h5oW-3P1BFG6d0Y0lMmB2IVnZ5tgbCOGvivfJzf-t8_ndvQxB-Zg'


# Load payloads from test.json
with open('org.json', 'r') as json_file:
    payloads = json.load(json_file)

# Load Excel data
df = pd.read_excel('orgPayload.xlsx')


# API endpoint
url = 'https://ig.aidtaas.com/market-place/v1.0/organisations'

# Headers including Authorization token
headers = {
    'Content-Type': 'application/json',
    'Authorization': token
}

responses = []
org_ids = []

# Iterate over each payload
for payload in payloads:
    try:
        # Make a POST request
        response = requests.post(url, json=payload, headers=headers)
        
        # Get the response status code and text
        response_status = response.status_code
        response_text = response.text
        
        # Check if the response status is 200 (OK)
        if response_status == 200:
            try:
                # Try to parse the response as JSON
                response_json = response.json()
                responses.append(response_json)
                org_ids.append(response_json['id'])
            except json.JSONDecodeError:
                # If response is not valid JSON
                responses.append(response_text)
                org_ids.append(response_text)
                print(f"Response is not valid JSON: {response_text}")
        else:
            # If response status is not 200, print error message
            responses.append(response_text)
            org_ids.append(response_text)
            print(f"Request failed with status code {response_status}: {response_text}")

    except requests.RequestException as e:
        # If request itself fails (e.g., network error)
        responses.append(e)
        org_ids.append(e)
        print(f"Request failed: {e}")

# Save responses to a file
with open('Orgresponses.json', 'w') as responses_file:
    json.dump(responses, responses_file, indent=4)

print("Responses saved successfully.")


# Add 'AccountID' column to DataFrame
df['OrgID'] = org_ids

# Write updated DataFrame back to the same Excel file
df.to_excel('orgPayload.xlsx', index=False)

print("Excel file updated with AccountIDs.")

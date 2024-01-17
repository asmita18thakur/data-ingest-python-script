import json
import requests
import pandas as pd

token = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImZmOGYxNjhmLTNmZjYtNDZlMi1iMTJlLWE2YTdlN2Y2YTY5MCJ9.eyJwcm9maWxlVXJsIjoid3d3Lmdvb2dsZS5jb20vbWVyYV9waWMvYXZpbmFzaC5wbmciLCJyZWNlbnRfc2Vzc2lvbiI6Ik5BIiwic3ViIjoiZ2FpYW4uY29tIiwicGFyZW50VGVuYW50SWQiOiJOQSIsImNvbG9yIjoicmVkIiwidXNlcl9uYW1lIjoidGVuYW50MTBAZ2F0ZXN0YXV0b21hdGlvbi5jb20iLCJpc3MiOiJnYWlhbi5jb20iLCJpc0FkbWluIjp0cnVlLCJwbGF0Zm9ybUlkIjoiNjA0Nzg5ZWI0MmI3ZGMwMDAxN2E4MzQxIiwidXNlck5hbWUiOiJ0ZW5hbnQxMEBnYXRlc3RhdXRvbWF0aW9uLmNvbSIsImF1dGhvcml0aWVzIjpbIlJPTEVfQ09OU1VNRVJfRkFDRUJPT0siLCJST0xFX01YX09QRVJBVE9SIl0sImNsaWVudF9pZCI6ImdhaWFuIiwic2NvcGUiOlsidHJ1c3QiLCJyZWFkIiwid3JpdGUiXSwidGVuYW50SWQiOiI2NGUxY2IzOTFmNmQ3ZjAwMDE2MWZiM2EiLCJsb2dvIjpudWxsLCJleHAiOjE2OTMxODgyODksImp0aSI6Ijc2ZWI0OGUxLWEwMTEtNDdkYS1iZDc0LTEyNTA3ZGU1OGIwZSIsImVtYWlsIjoidGVuYW50MTBAZ2F0ZXN0YXV0b21hdGlvbi5jb20ifQ.DlqEU8v045xoT6JNKeNoo2LOwb7L_RJT9XTb72gP_iEeIncG4EPlOBe78LuP1tbUO-WWjjYHKjQC7XU-r38-rTvMLVDrfuK8K9Jo4HenT-x9sxOee7nAq2h2RcTFWOxgtphIell37jGUZD5Hbl67o0UmgxxEEN7z6ccyS9E9WvSfwv5zMCmQi1v6dfknWc-4JDxXqTjsFA2RBZOBXTXMuWWMU8SqQct0tS9l6qMSArPH7bPiT-hZ5dX84x-LNBozaFkXe8DPOCKhXeoA9Sh7ntGkPpetp-R0VDX9npe6Huk_ZlAurl2tVoDBOUWJRUDbBk3SUxFykm_3guV6yO21TQ'


# Load payloads from test.json
with open('otp.json', 'r') as json_file:
    payloads = json.load(json_file)

# Load Excel data
df = pd.read_excel('otpPayload.xlsx')


# API endpoint
url = 'https://ig.aidtaas.com/iam-service/v1.0/tenants/otp-verification'

# Headers including Authorization token
headers = {
    'Content-Type': 'application/json',
}

responses = []
otp_ids = []

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
                otp_ids.append(response_json['tenantId'])
            except json.JSONDecodeError:
                # If response is not valid JSON
                responses.append(response_text)
                otp_ids.append(response_text)
                print(f"Response is not valid JSON: {response_text}")
        else:
            # If response status is not 200, print error message
            responses.append(response_text)
            otp_ids.append(response_text)
            print(f"Request failed with status code {response_status}: {response_text}")

    except requests.RequestException as e:
        # If request itself fails (e.g., network error)
        responses.append(e)
        otp_ids.append(e)
        print(f"Request failed: {e}")

# Save responses to a file
with open('otpResponse.json', 'w') as responses_file:
    json.dump(responses, responses_file, indent=4)

print("Responses saved successfully.")

# Add 'AccountID' column to DataFrame
df['TenantID'] = otp_ids

# Write updated DataFrame back to the same Excel file
df.to_excel('otpPayload.xlsx', index=False)

print("Excel file updated with tenantIDs.")

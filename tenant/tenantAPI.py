import json
import requests


token = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImZmOGYxNjhmLTNmZjYtNDZlMi1iMTJlLWE2YTdlN2Y2YTY5MCJ9.eyJwcm9maWxlVXJsIjoid3d3Lmdvb2dsZS5jb20vbWVyYV9waWMvYXZpbmFzaC5wbmciLCJyZWNlbnRfc2Vzc2lvbiI6Ik5BIiwic3ViIjoiZ2FpYW4uY29tIiwicGFyZW50VGVuYW50SWQiOiJOQSIsImNvbG9yIjoicmVkIiwidXNlcl9uYW1lIjoidGVuYW50MTBAZ2F0ZXN0YXV0b21hdGlvbi5jb20iLCJpc3MiOiJnYWlhbi5jb20iLCJpc0FkbWluIjp0cnVlLCJwbGF0Zm9ybUlkIjoiNjA0Nzg5ZWI0MmI3ZGMwMDAxN2E4MzQxIiwidXNlck5hbWUiOiJ0ZW5hbnQxMEBnYXRlc3RhdXRvbWF0aW9uLmNvbSIsImF1dGhvcml0aWVzIjpbIlJPTEVfQ09OU1VNRVJfRkFDRUJPT0siLCJST0xFX01YX09QRVJBVE9SIl0sImNsaWVudF9pZCI6ImdhaWFuIiwic2NvcGUiOlsidHJ1c3QiLCJyZWFkIiwid3JpdGUiXSwidGVuYW50SWQiOiI2NGUxY2IzOTFmNmQ3ZjAwMDE2MWZiM2EiLCJsb2dvIjpudWxsLCJleHAiOjE2OTMyNTgyNzIsImp0aSI6ImRkYzhjMjc1LTk5NjEtNGE5NC04NzBlLTAyNDZjMmYzNjUzZSIsImVtYWlsIjoidGVuYW50MTBAZ2F0ZXN0YXV0b21hdGlvbi5jb20ifQ.azAyBydw8gry2QVbjc8yS-peAHJ1yTdqDD0VOhvrKD6d_DbimoUj2VWSVCrPKotJxxuojTnTvhb1V4_ZmSBO2DiQmL2f0lt0AU8-89oJ0ofC66aCEsjEe53E9x4bumFcOqim0EvMLIBFCGo8DBjB99-h7cUedPr7YhMEr-goSqzI5t6Z2B3HjFCmRgAGfrrrrnJ_DaWrMjzWHDCnyVE1r_ZZEdhwbLgHTiMykJ8yuHCNE8dPPWd6ldtqQ-PhhyUMajG8KC3mFRn2IFNDxwdSQw29QU7SKOp-kIyWnB2DQFXg5REf_V1bySbBiJayxHyzDBJ8xzrysaoAISu7BcbO3A'


# # Load payloads from test.json
with open('tenant.json', 'r') as json_file:
    payloads = json.load(json_file)


# API endpoint
url = 'https://ig.aidtaas.com/market-place/v1.0/tenants'

# Headers including Authorization token
headers = {
    'Content-Type': 'application/json',
    'Authorization': token
}

responses = []

# Iterate over each payload
for payload in payloads:
    # print(payload)
    try:
        # Make a POST request
        response = requests.post(url, json=payload, headers=headers)
        
        # Get the response status code and text
        response_status = response.status_code
        response_text = response.json()
        # print("hiiii",response.json())
        
        # Check if the response status is 200 (OK)
        if response_status == 201:
            try:
                # Try to parse the response as JSON
                response_json = response.json()
                responses.append(response_json)
                
            except json.JSONDecodeError:
                # If response is not valid JSON
                responses.append(response_text)
                print(f"Response is not valid JSON: {response_text}")
        else:
            # If response status is not 200, print error message
            responses.append(response_text)
            print(f"Request failed with status code {response_status}: {response_text}")

    except requests.RequestException as e:
        # If request itself fails (e.g., network error)
        responses.append(e)
        print(f"Request failed: {e}")

# Save responses to a file
with open('tenantResponse.json', 'w') as responses_file:
    json.dump(responses, responses_file, indent=4)

print("Responses saved successfully.")

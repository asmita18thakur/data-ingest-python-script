import json
import requests
import pandas as pd

token = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI3Ny1NUVdFRTNHZE5adGlsWU5IYmpsa2dVSkpaWUJWVmN1UmFZdHl5ejFjIn0.eyJleHAiOjE3MjYyMDY2MTQsImlhdCI6MTcyNjE3MDYxNCwianRpIjoiNmY3NDc0YmUtMDcxNS00ZmE3LWI5ZWMtOWM1NGY5YTViN2FhIiwiaXNzIjoiaHR0cDovL2tleWNsb2FrLmtleWNsb2FrLnN2Yy5jbHVzdGVyLmxvY2FsOjgwODAvcmVhbG1zL21hc3RlciIsImF1ZCI6WyJCT0xUWk1BTk5fQk9UIiwiUEFTQ0FMX0lOVEVMTElHRU5DRSIsIlhQWC1DTVMiLCJhY2NvdW50Il0sInN1YiI6IjdjMmEwY2M1LTY5ODgtNDk5OS04ZjZkLTQ4MjM2MzQ4MmVlZiIsInR5cCI6IkJlYXJlciIsImF6cCI6IkhPTEFDUkFDWSIsInNlc3Npb25fc3RhdGUiOiI5ZTBhYjZlNS0yNmI5LTRkOWItODA4ZC0wY2Q0MWU3ZWMyMDUiLCJuYW1lIjoibW9iaXVzIG1vYml1cyIsImdpdmVuX25hbWUiOiJtb2JpdXMiLCJmYW1pbHlfbmFtZSI6Im1vYml1cyIsInByZWZlcnJlZF91c2VybmFtZSI6InBhc3N3b3JkX3RlbmFudF9tb2JpdXNAbW9iaXVzZHRhYXMuYWkiLCJlbWFpbCI6InBhc3N3b3JkX3RlbmFudF9tb2JpdXNAbW9iaXVzZHRhYXMuYWkiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYWNyIjoiMSIsImFsbG93ZWQtb3JpZ2lucyI6WyIvKiJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsiZGVmYXVsdC1yb2xlcy1tYXN0ZXIiLCJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiQk9MVFpNQU5OX0JPVCI6eyJyb2xlcyI6WyJCT0xUWk1BTk5fQk9UX1VTRVIiXX0sIlBBU0NBTF9JTlRFTExJR0VOQ0UiOnsicm9sZXMiOlsiU1VQRVJBRE1JTiJdfSwiWFBYLUNNUyI6eyJyb2xlcyI6WyJYUFgtQ01TX1VTRVIiXX0sIkhPTEFDUkFDWSI6eyJyb2xlcyI6WyJIT0xBQ1JBQ1lfVVNFUiJdfSwiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJwcm9maWxlIGVtYWlsIiwic2lkIjoiOWUwYWI2ZTUtMjZiOS00ZDliLTgwOGQtMGNkNDFlN2VjMjA1IiwidGVuYW50SWQiOiI3YzJhMGNjNS02OTg4LTQ5OTktOGY2ZC00ODIzNjM0ODJlZWYiLCJyZXF1ZXN0ZXJUeXBlIjoiVEVOQU5UIn0=.R4L6stW_Iv-yxf3FeTG5wwoCRD6YpialiDxo1Z1JCsQ168mkhuuFnNRHvyTxHb7DTZBSqjP6wlMsauOR-g9cyuVPx1lKNo4q4cp54AE8gLX09Vw0PqOh103XNaP6-iEClgDPzJgobIE7xGp2Gg7b2ZqqcLe1smiUzy9mUCTyAJRE-7O8FpXLdyJy-jfWGz8eed2-s1ffHIaOXKbWRUjR58mvxTG0ZAwM-1mNuW4eGRJS0QTMYPsYT9bO8PzYdlubl1cFCKmz47x-rlTlyepXesLgw9BYIJCMMCMT1N9T7yejdi_pTBWYismNFRWx6gGYX7cxasAKRernr-RZnHvWMg'


# # Load payloads from test.json
with open('product.json', 'r') as json_file:
    payloads = json.load(json_file)

# Load Excel data
df = pd.read_excel('productCreation.xlsx')


# API endpoint
url = 'https://ig.gov-cloud.ai/hcy-web/v1.0/products?requiredMasterConfigId=false'

# Headers including Authorization token
headers = {
    'Content-Type': 'application/json',
    'Authorization': token
}

responses = []
product_ids = []

# Iterate over each payload
for payload in payloads:
    try:
        print(payload)
        # Make a POST request
        response = requests.post(url, json=payload, headers=headers)
        
        # Get the response status code and text
        response_status = response.status_code
        response_text = response.text
        
        # Check if the response status is 200 (OK)
        if response_status == 201:
            try:
                # Try to parse the response as JSON
                response_json = response.json()
                responses.append(response_json)
                product_ids.append(response_json['id'])
            except json.JSONDecodeError:
                # If response is not valid JSON
                responses.append(response_text)
                product_ids.append(response_text)
                print(f"Response is not valid JSON: {response_text}")
        else:
            # If response status is not 200, print error message
            responses.append(response_text)
            product_ids.append(response_text)
            print(f"Request failed with status code {response_status}: {response_text}")

    except requests.RequestException as e:
        # If request itself fails (e.g., network error)
        responses.append(e)
        product_ids.append(e)
        print(f"Request failed: {e}")

# Save responses to a file
with open('productResponse.json', 'w') as responses_file:
    json.dump(responses, responses_file, indent=4)

print("Responses saved successfully.")
print(product_ids)

# Add 'AccountID' column to DataFrame
df['productID'] = product_ids

# Write updated DataFrame back to the same Excel file
df.to_excel('productCreation.xlsx', index=False)

print("Excel file updated with productIDs.")

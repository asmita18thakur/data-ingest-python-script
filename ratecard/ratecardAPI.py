import json
import requests
import pandas as pd
import ast

# ============================


def is_valid_json(data):
    try:
        json.loads(data)
        return True
    except ValueError:
        return False

# Test examples
json_data = '{"name": "John", "age": 30, "city": "New York"}'
non_json_data = 'This is not JSON'


# =================================




# Load Excel data
df = pd.read_excel('ratecards.xlsx')



# Headers including Authorization token
headers = {
    'Content-Type': 'application/json',
    'authorization':'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI3Ny1NUVdFRTNHZE5adGlsWU5IYmpsa2dVSkpaWUJWVmN1UmFZdHl5ejFjIn0.eyJleHAiOjE3MjYyMDY2MTQsImlhdCI6MTcyNjE3MDYxNCwianRpIjoiNmY3NDc0YmUtMDcxNS00ZmE3LWI5ZWMtOWM1NGY5YTViN2FhIiwiaXNzIjoiaHR0cDovL2tleWNsb2FrLmtleWNsb2FrLnN2Yy5jbHVzdGVyLmxvY2FsOjgwODAvcmVhbG1zL21hc3RlciIsImF1ZCI6WyJCT0xUWk1BTk5fQk9UIiwiUEFTQ0FMX0lOVEVMTElHRU5DRSIsIlhQWC1DTVMiLCJhY2NvdW50Il0sInN1YiI6IjdjMmEwY2M1LTY5ODgtNDk5OS04ZjZkLTQ4MjM2MzQ4MmVlZiIsInR5cCI6IkJlYXJlciIsImF6cCI6IkhPTEFDUkFDWSIsInNlc3Npb25fc3RhdGUiOiI5ZTBhYjZlNS0yNmI5LTRkOWItODA4ZC0wY2Q0MWU3ZWMyMDUiLCJuYW1lIjoibW9iaXVzIG1vYml1cyIsImdpdmVuX25hbWUiOiJtb2JpdXMiLCJmYW1pbHlfbmFtZSI6Im1vYml1cyIsInByZWZlcnJlZF91c2VybmFtZSI6InBhc3N3b3JkX3RlbmFudF9tb2JpdXNAbW9iaXVzZHRhYXMuYWkiLCJlbWFpbCI6InBhc3N3b3JkX3RlbmFudF9tb2JpdXNAbW9iaXVzZHRhYXMuYWkiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYWNyIjoiMSIsImFsbG93ZWQtb3JpZ2lucyI6WyIvKiJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsiZGVmYXVsdC1yb2xlcy1tYXN0ZXIiLCJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiQk9MVFpNQU5OX0JPVCI6eyJyb2xlcyI6WyJCT0xUWk1BTk5fQk9UX1VTRVIiXX0sIlBBU0NBTF9JTlRFTExJR0VOQ0UiOnsicm9sZXMiOlsiU1VQRVJBRE1JTiJdfSwiWFBYLUNNUyI6eyJyb2xlcyI6WyJYUFgtQ01TX1VTRVIiXX0sIkhPTEFDUkFDWSI6eyJyb2xlcyI6WyJIT0xBQ1JBQ1lfVVNFUiJdfSwiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJwcm9maWxlIGVtYWlsIiwic2lkIjoiOWUwYWI2ZTUtMjZiOS00ZDliLTgwOGQtMGNkNDFlN2VjMjA1IiwidGVuYW50SWQiOiI3YzJhMGNjNS02OTg4LTQ5OTktOGY2ZC00ODIzNjM0ODJlZWYiLCJyZXF1ZXN0ZXJUeXBlIjoiVEVOQU5UIn0=.R4L6stW_Iv-yxf3FeTG5wwoCRD6YpialiDxo1Z1JCsQ168mkhuuFnNRHvyTxHb7DTZBSqjP6wlMsauOR-g9cyuVPx1lKNo4q4cp54AE8gLX09Vw0PqOh103XNaP6-iEClgDPzJgobIE7xGp2Gg7b2ZqqcLe1smiUzy9mUCTyAJRE-7O8FpXLdyJy-jfWGz8eed2-s1ffHIaOXKbWRUjR58mvxTG0ZAwM-1mNuW4eGRJS0QTMYPsYT9bO8PzYdlubl1cFCKmz47x-rlTlyepXesLgw9BYIJCMMCMT1N9T7yejdi_pTBWYismNFRWx6gGYX7cxasAKRernr-RZnHvWMg'
}

responses = []
ratecard_ids = []
# Iterate over each payload
for index, row in df.iterrows():
    print(row['productID'])

    # API endpoint
    url = 'https://ig.gov-cloud.ai/hcy-web/v1.0/rate-cards/product/'+ str(row['productID'])
    print(url)
    try:
        json_payload = json.loads(row['json'])
    except json.JSONDecodeError:
        try:
            json_payload = ast.literal_eval(row['json'])
        except (SyntaxError, ValueError):
            print(f"Malformed JSON at index {index}: {row['json']}")
            responses.append("error")
            ratecard_ids.append("error")
            continue  # Move to the next iteration
    
    response = requests.post(url, json=json_payload, headers=headers)
    response_json = response.json()
    responses.append(response_json)
    
    if response.status_code == 201:
        ratecard_ids.append(response_json.get('id', ''))
        # print("Successfully created:", response_json)
    else:
        ratecard_ids.append("error")
        print("Error response:", response.status_code, response_json)


# Save responses to a file
with open('rateCardResponse.json', 'w') as responses_file:
    json.dump(responses, responses_file, indent=4)

print("Responses saved successfully.")

# Add 'AccountID' column to DataFrame
df['RateCardID'] = ratecard_ids

# Write updated DataFrame back to the same Excel file
df.to_excel('ratecards.xlsx', index=False)

print("Excel file updated with ratecardIDS")


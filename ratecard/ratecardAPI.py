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


# =================================

# Load payloads from account.json
with open('ratecard.json', 'r') as json_file:
    payloads = json.load(json_file)

print(payloads)
# Load Excel data
df = pd.read_excel('rate_card.xlsx')



# Headers including Authorization token
headers = {
    'Content-Type': 'application/json',
    'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI3Ny1NUVdFRTNHZE5adGlsWU5IYmpsa2dVSkpaWUJWVmN1UmFZdHl5ejFjIn0.eyJleHAiOjE3MjMyNDI1ODQsImlhdCI6MTcyMzIwNjU4NCwianRpIjoiNjcxYWQ5NmQtNGExNC00N2MyLTlmZmUtMmM0NjNkZmU0MzA1IiwiaXNzIjoiaHR0cDovL2tleWNsb2FrLmtleWNsb2FrLnN2Yy5jbHVzdGVyLmxvY2FsOjgwODAvcmVhbG1zL21hc3RlciIsImF1ZCI6WyJCT0xUWk1BTk5fQk9UIiwiUEFTQ0FMX0lOVEVMTElHRU5DRSIsIk1PTkVUIiwiYWNjb3VudCIsIlZJTkNJIl0sInN1YiI6IjMwMzdkZjZiLWE0YTUtNDE1Ni1hMTI4LWQwZTdkYTM5YzA3OCIsInR5cCI6IkJlYXJlciIsImF6cCI6IkhPTEFDUkFDWSIsInNlc3Npb25fc3RhdGUiOiIxZjQzYjBhOS03MDU2LTRiMGEtODUxZC0yMjg2NzY1YWJlMTgiLCJuYW1lIjoibW9iaXVzIG1vYml1cyIsImdpdmVuX25hbWUiOiJtb2JpdXMiLCJmYW1pbHlfbmFtZSI6Im1vYml1cyIsInByZWZlcnJlZF91c2VybmFtZSI6InBhc3N3b3JkX3RlbmFudF9tb2JpdXNAbW9iaXVzZHRhYXMuYWkiLCJlbWFpbCI6InBhc3N3b3JkX3RlbmFudF9tb2JpdXNAbW9iaXVzZHRhYXMuYWkiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYWNyIjoiMSIsImFsbG93ZWQtb3JpZ2lucyI6WyIvKiJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsiZGVmYXVsdC1yb2xlcy1tYXN0ZXIiLCJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiQk9MVFpNQU5OX0JPVCI6eyJyb2xlcyI6WyJCT0xUWk1BTk5fQk9UX1VTRVIiXX0sIlBBU0NBTF9JTlRFTExJR0VOQ0UiOnsicm9sZXMiOlsiUEFTQ0FMX0lOVEVMTElHRU5DRV9VU0VSIiwiUEFTQ0FMX0lOVEVMTElHRU5DRV9BRE1JTiJdfSwiTU9ORVQiOnsicm9sZXMiOlsiTU9ORVRfVVNFUiJdfSwiSE9MQUNSQUNZIjp7InJvbGVzIjpbIlNVUEVSQURNSU4iLCJIT0xBQ1JBQ1lfVVNFUiJdfSwiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19LCJWSU5DSSI6eyJyb2xlcyI6WyJWSU5DSV9VU0VSIl19fSwic2NvcGUiOiJwcm9maWxlIGVtYWlsIiwic2lkIjoiMWY0M2IwYTktNzA1Ni00YjBhLTg1MWQtMjI4Njc2NWFiZTE4IiwidGVuYW50SWQiOiIzMDM3ZGY2Yi1hNGE1LTQxNTYtYTEyOC1kMGU3ZGEzOWMwNzgifQ==.MNFu9g1tqyiNr3-4tHPFeOjlNdmhNkbgM3JVEpqBGXzlbjHlrAw0xXLESdq6Y7-ncP06mxKCY53NevQIt5HTcRQTaT6fMoIwPHUSlKAM-R7tZjTK-AoY9YRAdvdsQoQF3WpJd5A0JYVxyOXaIYtcuoD8EKGZfV2e-4kbeYG8wKbMPOMj84ejRAcR9PYnMNOZi0xb8KPsF-AS-EKjQSJXoKh1F4FU9Uh_FS-Z7YlrtGyfTsTYoj-AhmoNBxH-sFWSZGQ8hgoX0WKt8BDsYWnAl98g_5dgEPS59kGl0iPvZgZ6k_IZy04If-yvSaIf45y2tXyqbKPgAjlGtu6h14ZvAw'
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
    
    # Send the POST request to the API
    response = requests.post(url, json=payloads, headers=headers)
    if response.status_code == 201:
        # Successfully created ratecard, extract ID
        response_json = response.json()
        ratecard_id = response_json.get('id', 'No ID returned')
        ratecard_ids.append(ratecard_id)
        responses.append(response_json)
        print(f"Successfully created ratecard with ID: {ratecard_id}")
    else:
        # Log error details if the API call was unsuccessful
        print(f"Error response at index {index}: {response.status_code} - {response.text}")
        responses.append(response.text)
        ratecard_ids.append("error")

# Save responses to a JSON file
with open('rateCardResponse.json', 'w') as file:
    json.dump(responses, file, indent=4)
print("Responses saved successfully.")

# Update the DataFrame with new ratecard IDs
df['RateCardID'] = ratecard_ids

# Write updated DataFrame back to the same Excel file
df.to_excel('ratecardresponse.xlsx', index=False)

print("Excel file updated with ratecardIDS")


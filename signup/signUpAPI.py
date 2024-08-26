import json
import requests
import pandas as pd

token = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI3Ny1NUVdFRTNHZE5adGlsWU5IYmpsa2dVSkpaWUJWVmN1UmFZdHl5ejFjIn0.eyJleHAiOjE3MjMyNDI1ODQsImlhdCI6MTcyMzIwNjU4NCwianRpIjoiNjcxYWQ5NmQtNGExNC00N2MyLTlmZmUtMmM0NjNkZmU0MzA1IiwiaXNzIjoiaHR0cDovL2tleWNsb2FrLmtleWNsb2FrLnN2Yy5jbHVzdGVyLmxvY2FsOjgwODAvcmVhbG1zL21hc3RlciIsImF1ZCI6WyJCT0xUWk1BTk5fQk9UIiwiUEFTQ0FMX0lOVEVMTElHRU5DRSIsIk1PTkVUIiwiYWNjb3VudCIsIlZJTkNJIl0sInN1YiI6IjMwMzdkZjZiLWE0YTUtNDE1Ni1hMTI4LWQwZTdkYTM5YzA3OCIsInR5cCI6IkJlYXJlciIsImF6cCI6IkhPTEFDUkFDWSIsInNlc3Npb25fc3RhdGUiOiIxZjQzYjBhOS03MDU2LTRiMGEtODUxZC0yMjg2NzY1YWJlMTgiLCJuYW1lIjoibW9iaXVzIG1vYml1cyIsImdpdmVuX25hbWUiOiJtb2JpdXMiLCJmYW1pbHlfbmFtZSI6Im1vYml1cyIsInByZWZlcnJlZF91c2VybmFtZSI6InBhc3N3b3JkX3RlbmFudF9tb2JpdXNAbW9iaXVzZHRhYXMuYWkiLCJlbWFpbCI6InBhc3N3b3JkX3RlbmFudF9tb2JpdXNAbW9iaXVzZHRhYXMuYWkiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYWNyIjoiMSIsImFsbG93ZWQtb3JpZ2lucyI6WyIvKiJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsiZGVmYXVsdC1yb2xlcy1tYXN0ZXIiLCJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiQk9MVFpNQU5OX0JPVCI6eyJyb2xlcyI6WyJCT0xUWk1BTk5fQk9UX1VTRVIiXX0sIlBBU0NBTF9JTlRFTExJR0VOQ0UiOnsicm9sZXMiOlsiUEFTQ0FMX0lOVEVMTElHRU5DRV9VU0VSIiwiUEFTQ0FMX0lOVEVMTElHRU5DRV9BRE1JTiJdfSwiTU9ORVQiOnsicm9sZXMiOlsiTU9ORVRfVVNFUiJdfSwiSE9MQUNSQUNZIjp7InJvbGVzIjpbIlNVUEVSQURNSU4iLCJIT0xBQ1JBQ1lfVVNFUiJdfSwiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19LCJWSU5DSSI6eyJyb2xlcyI6WyJWSU5DSV9VU0VSIl19fSwic2NvcGUiOiJwcm9maWxlIGVtYWlsIiwic2lkIjoiMWY0M2IwYTktNzA1Ni00YjBhLTg1MWQtMjI4Njc2NWFiZTE4IiwidGVuYW50SWQiOiIzMDM3ZGY2Yi1hNGE1LTQxNTYtYTEyOC1kMGU3ZGEzOWMwNzgifQ==.MNFu9g1tqyiNr3-4tHPFeOjlNdmhNkbgM3JVEpqBGXzlbjHlrAw0xXLESdq6Y7-ncP06mxKCY53NevQIt5HTcRQTaT6fMoIwPHUSlKAM-R7tZjTK-AoY9YRAdvdsQoQF3WpJd5A0JYVxyOXaIYtcuoD8EKGZfV2e-4kbeYG8wKbMPOMj84ejRAcR9PYnMNOZi0xb8KPsF-AS-EKjQSJXoKh1F4FU9Uh_FS-Z7YlrtGyfTsTYoj-AhmoNBxH-sFWSZGQ8hgoX0WKt8BDsYWnAl98g_5dgEPS59kGl0iPvZgZ6k_IZy04If-yvSaIf45y2tXyqbKPgAjlGtu6h14ZvAw'


# Load payloads from test.json
with open('signUp.json', 'r') as json_file:
    payloads = json.load(json_file)


# # Load payloads from test.json
# with open('Accountpayload.json', 'r') as json_file:
#     payloads = json.load(json_file)


# API endpoint
# url = 'https://ig.aidtaas.com/iam-service/v1.0/tenants/signup'
url = 'https://ig.gov-cloud.ai/mobius-iam-service/v1.0/emails/sign-up'

# Headers including Authorization token
headers = {
    'Content-Type': 'application/json',
}

responses = []

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
        print(f"Request failed: {e}")
        responses.append(e)

# Save responses to a file
with open('signUpResponse.json', 'w') as responses_file:
    json.dump(responses, responses_file, indent=4)

print("Responses saved successfully.")

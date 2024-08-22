import pandas as pd
import requests
import math
import json


# Load the Excel file
file_path = 'marketPlaces.xlsx'  # Path to your Excel file
df = pd.read_excel(file_path)

# URL of the API endpoint
url = 'https://ig.gov-cloud.ai/hcy-web/v1.0/platforms'
payloads = []

# Iterate over each row in the DataFrame
response_ids = []
for index, row in df.iterrows():
    payload = {
        "name": row['name'],
        "description": row['description'],
         "icon": "https://www.google.com/",
        "title": "Google",
        "currencies": row['currencies'].split(','),  # Assuming comma-separated string in Excel
        "ownerId": row['ownerId'],
        "config": {},  # Modify as needed
        "mxUrl": row['mxUrl'],
        "serpLocation": {},  # Modify as needed
        "parentPlatformId": row['parentPlatformId'],
        "platformConfig": {},  # Modify as needed
        "platformMasterConfig": {
            "mission": row['mission'],
            "vision": row['vision'],
            "values": row['values'].split(','),  # Assuming comma-separated string in Excel
            "legalBusinessname": row['legalBusinessname'],
            "organisationLogo": row['organisationLogo'],
            "businessregistrationNumber": row['businessregistrationNumber'],
            "businessAddress": row['businessAddress'],
            "postalCode": row['postalCode'],
            "city": row['city'],
            "state": row['state'],
            "emailId": row['emailId'],
            "contactNumber": "45664653",
            "cikKey": "545",
            "crunchBaseUrl": "45646555",
            "nationalBbbId": "4564565",
            "regionalBbbId": "568765132",
           "themeColourPrimary":"#FFFFF",
            "themeColourSecondary":"#FFFFF",
            "themeColourBackGround":"#FFFF",
            "themeColourText":"#FFFF",
            "themeIcons":"Flex Line",
            "themeFontHeading":"Lato",
            "themeFontBody":"Loto",
            "allowPersonalisation":'true',
            "loginThemeColour":"#FFFF",
            "loginImage":"https://media.licdn.com/dms/image/C510BAQGNxm-cQ3-WcA/company-logo_200_200/0/1569563107210?e=2147483647&v=beta&t=eVl9vEFsun42_l7ZPDS6BosDnK-XkdoeNG37K338lhY",
            "errorThemeColour":"#FFFF",
            "errorImage":"https://img.freepik.com/free-vector/glitch-error-404-page-background_23-2148072533.jpg",
            "storeFrontThemeColour":"#FFFF",
            "storeFrontImage":"abc",
            "productThemeColour":"#FFFF",
            "productImage":"abc",
            "productListingType":"Compact",
            "productListingBackground":"abc",
            "allowNatureMarketPlace":'true',
            "NatureMarketPlaceType":"Traditional",
            "allowMarketPlaceType":'true',
            "marketPlaceType":"Org Public",
            "allowInvitesExpire":'true',
            "invitesExpire":"30Days",
            "allowCommunicate":'true',
            "allowTenantToAdd":'true',
            "newParticipants":[
                "XP only",
                "More than 10 alliances"
            ],
            "allowTypeOfTenants":'true',
            "typeOfTenants":[
                "All types"
            ],
            "requireCoolDown":'true',
            "coolDownPeriod":"1month",
            "allowAllianceFormation":'true',
            "allianceOperatorApproval":[
                "Always",
                "Tenants <365days old"
            ],
            "requireApprovalExit":'true',
            "exitAlliance":[
                "For ARR >300k USD",
                "For ARR >100k USD"
            ],
            "dissolveAlliance":"Operator only"

        }
    }

    payloads.append(payload)

    with open('marketplaces.json', 'w') as json_file:
        json.dump(payload, json_file, indent=4)

    # Send the POST request
    headers = {
        'Content-Type': 'application/json',
        'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI3Ny1NUVdFRTNHZE5adGlsWU5IYmpsa2dVSkpaWUJWVmN1UmFZdHl5ejFjIn0.eyJleHAiOjE3MjMyNDI1ODQsImlhdCI6MTcyMzIwNjU4NCwianRpIjoiNjcxYWQ5NmQtNGExNC00N2MyLTlmZmUtMmM0NjNkZmU0MzA1IiwiaXNzIjoiaHR0cDovL2tleWNsb2FrLmtleWNsb2FrLnN2Yy5jbHVzdGVyLmxvY2FsOjgwODAvcmVhbG1zL21hc3RlciIsImF1ZCI6WyJCT0xUWk1BTk5fQk9UIiwiUEFTQ0FMX0lOVEVMTElHRU5DRSIsIk1PTkVUIiwiYWNjb3VudCIsIlZJTkNJIl0sInN1YiI6IjMwMzdkZjZiLWE0YTUtNDE1Ni1hMTI4LWQwZTdkYTM5YzA3OCIsInR5cCI6IkJlYXJlciIsImF6cCI6IkhPTEFDUkFDWSIsInNlc3Npb25fc3RhdGUiOiIxZjQzYjBhOS03MDU2LTRiMGEtODUxZC0yMjg2NzY1YWJlMTgiLCJuYW1lIjoibW9iaXVzIG1vYml1cyIsImdpdmVuX25hbWUiOiJtb2JpdXMiLCJmYW1pbHlfbmFtZSI6Im1vYml1cyIsInByZWZlcnJlZF91c2VybmFtZSI6InBhc3N3b3JkX3RlbmFudF9tb2JpdXNAbW9iaXVzZHRhYXMuYWkiLCJlbWFpbCI6InBhc3N3b3JkX3RlbmFudF9tb2JpdXNAbW9iaXVzZHRhYXMuYWkiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYWNyIjoiMSIsImFsbG93ZWQtb3JpZ2lucyI6WyIvKiJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsiZGVmYXVsdC1yb2xlcy1tYXN0ZXIiLCJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiQk9MVFpNQU5OX0JPVCI6eyJyb2xlcyI6WyJCT0xUWk1BTk5fQk9UX1VTRVIiXX0sIlBBU0NBTF9JTlRFTExJR0VOQ0UiOnsicm9sZXMiOlsiUEFTQ0FMX0lOVEVMTElHRU5DRV9VU0VSIiwiUEFTQ0FMX0lOVEVMTElHRU5DRV9BRE1JTiJdfSwiTU9ORVQiOnsicm9sZXMiOlsiTU9ORVRfVVNFUiJdfSwiSE9MQUNSQUNZIjp7InJvbGVzIjpbIlNVUEVSQURNSU4iLCJIT0xBQ1JBQ1lfVVNFUiJdfSwiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19LCJWSU5DSSI6eyJyb2xlcyI6WyJWSU5DSV9VU0VSIl19fSwic2NvcGUiOiJwcm9maWxlIGVtYWlsIiwic2lkIjoiMWY0M2IwYTktNzA1Ni00YjBhLTg1MWQtMjI4Njc2NWFiZTE4IiwidGVuYW50SWQiOiIzMDM3ZGY2Yi1hNGE1LTQxNTYtYTEyOC1kMGU3ZGEzOWMwNzgifQ==.MNFu9g1tqyiNr3-4tHPFeOjlNdmhNkbgM3JVEpqBGXzlbjHlrAw0xXLESdq6Y7-ncP06mxKCY53NevQIt5HTcRQTaT6fMoIwPHUSlKAM-R7tZjTK-AoY9YRAdvdsQoQF3WpJd5A0JYVxyOXaIYtcuoD8EKGZfV2e-4kbeYG8wKbMPOMj84ejRAcR9PYnMNOZi0xb8KPsF-AS-EKjQSJXoKh1F4FU9Uh_FS-Z7YlrtGyfTsTYoj-AhmoNBxH-sFWSZGQ8hgoX0WKt8BDsYWnAl98g_5dgEPS59kGl0iPvZgZ6k_IZy04If-yvSaIf45y2tXyqbKPgAjlGtu6h14ZvAw'
    }
    response = requests.post(url, json=payload, headers=headers)
    response_json = response.json()
    # Store the response ID or an error message
    if response.status_code == 200:
        response_id = response_json.get('id', 'No ID in response')
        response_ids.append(response_id)
    else:
        response_ids.append(f"Error: {response.status_code}")
        print(response_json)

# Add the response IDs to the DataFrame
df['response_id'] = response_ids

with open('marketplaces.json', 'w') as json_file:
    json.dump(payloads, json_file, indent=4)

# Save the DataFrame back to the Excel file
df.to_excel(file_path, index=False)

print("Script completed. Response IDs have been written to the Excel file.")

import requests
import pandas as pd
import json

# API endpoint and headers
url = 'https://ig.gov-cloud.ai/hcy-web/v1.0/product/platform/filter?platformId=664afc3caf2dfa4e7eeda5db&productOffering=PRODUCT&size=50&page=0'
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI3Ny1NUVdFRTNHZE5adGlsWU5IYmpsa2dVSkpaWUJWVmN1UmFZdHl5ejFjIn0.eyJleHAiOjE3MjMyNDI1ODQsImlhdCI6MTcyMzIwNjU4NCwianRpIjoiNjcxYWQ5NmQtNGExNC00N2MyLTlmZmUtMmM0NjNkZmU0MzA1IiwiaXNzIjoiaHR0cDovL2tleWNsb2FrLmtleWNsb2FrLnN2Yy5jbHVzdGVyLmxvY2FsOjgwODAvcmVhbG1zL21hc3RlciIsImF1ZCI6WyJCT0xUWk1BTk5fQk9UIiwiUEFTQ0FMX0lOVEVMTElHRU5DRSIsIk1PTkVUIiwiYWNjb3VudCIsIlZJTkNJIl0sInN1YiI6IjMwMzdkZjZiLWE0YTUtNDE1Ni1hMTI4LWQwZTdkYTM5YzA3OCIsInR5cCI6IkJlYXJlciIsImF6cCI6IkhPTEFDUkFDWSIsInNlc3Npb25fc3RhdGUiOiIxZjQzYjBhOS03MDU2LTRiMGEtODUxZC0yMjg2NzY1YWJlMTgiLCJuYW1lIjoibW9iaXVzIG1vYml1cyIsImdpdmVuX25hbWUiOiJtb2JpdXMiLCJmYW1pbHlfbmFtZSI6Im1vYml1cyIsInByZWZlcnJlZF91c2VybmFtZSI6InBhc3N3b3JkX3RlbmFudF9tb2JpdXNAbW9iaXVzZHRhYXMuYWkiLCJlbWFpbCI6InBhc3N3b3JkX3RlbmFudF9tb2JpdXNAbW9iaXVzZHRhYXMuYWkiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYWNyIjoiMSIsImFsbG93ZWQtb3JpZ2lucyI6WyIvKiJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsiZGVmYXVsdC1yb2xlcy1tYXN0ZXIiLCJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiQk9MVFpNQU5OX0JPVCI6eyJyb2xlcyI6WyJCT0xUWk1BTk5fQk9UX1VTRVIiXX0sIlBBU0NBTF9JTlRFTExJR0VOQ0UiOnsicm9sZXMiOlsiUEFTQ0FMX0lOVEVMTElHRU5DRV9VU0VSIiwiUEFTQ0FMX0lOVEVMTElHRU5DRV9BRE1JTiJdfSwiTU9ORVQiOnsicm9sZXMiOlsiTU9ORVRfVVNFUiJdfSwiSE9MQUNSQUNZIjp7InJvbGVzIjpbIlNVUEVSQURNSU4iLCJIT0xBQ1JBQ1lfVVNFUiJdfSwiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19LCJWSU5DSSI6eyJyb2xlcyI6WyJWSU5DSV9VU0VSIl19fSwic2NvcGUiOiJwcm9maWxlIGVtYWlsIiwic2lkIjoiMWY0M2IwYTktNzA1Ni00YjBhLTg1MWQtMjI4Njc2NWFiZTE4IiwidGVuYW50SWQiOiIzMDM3ZGY2Yi1hNGE1LTQxNTYtYTEyOC1kMGU3ZGEzOWMwNzgifQ==.MNFu9g1tqyiNr3-4tHPFeOjlNdmhNkbgM3JVEpqBGXzlbjHlrAw0xXLESdq6Y7-ncP06mxKCY53NevQIt5HTcRQTaT6fMoIwPHUSlKAM-R7tZjTK-AoY9YRAdvdsQoQF3WpJd5A0JYVxyOXaIYtcuoD8EKGZfV2e-4kbeYG8wKbMPOMj84ejRAcR9PYnMNOZi0xb8KPsF-AS-EKjQSJXoKh1F4FU9Uh_FS-Z7YlrtGyfTsTYoj-AhmoNBxH-sFWSZGQ8hgoX0WKt8BDsYWnAl98g_5dgEPS59kGl0iPvZgZ6k_IZy04If-yvSaIf45y2tXyqbKPgAjlGtu6h14ZvAw'
}

# Send the request to the API
response = requests.get(url, headers=headers)

# Check if the response was successful
if response.status_code == 200:
    data = response.json()  # Parse the JSON response
    with open('productResponse.json', 'w') as json_file :
        json.dump(data, json_file, indent=2)
    # Assuming the data contains a list of products in a key called 'products'
    if 'content' in data and data['content']:
        # Convert the JSON data into a DataFrame
        df = pd.DataFrame(data['content'])
        
        # Write the data to an Excel file
        df.to_excel('products.xlsx', index=False)
        print("Data written to 'products.xlsx'")
    else:
        print("No 'content' found in the API response or the content is empty.")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
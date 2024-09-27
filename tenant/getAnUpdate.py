import pandas as pd
import requests
import json

# Load Excel data
df = pd.read_excel('update tenant Data.xlsx')  # Change 'tenant_data.xlsx' to the path of your file

# API endpoints
get_url = 'https://ig.gov-cloud.ai/hcy-web/v1.0/tenants/platforms?platformId=664afc3caf2dfa4e7eeda5db&size=100'

# Headers
headers = {
    'Content-Type': 'application/json',
    "Authorization": f"Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJhYktCMjBIbEhpclVudTJub1JHclRGSlJibXVqNGIzVlFXa1YwbThTYzZjIn0.eyJleHAiOjE3MTM1MzYyNzUsImlhdCI6MTcxMzUwMDI3NSwianRpIjoiMjVkNWY3MDAtN2ZkYy00ZTRlLWI5ODItMGZiZTBiY2IwMjk3IiwiaXNzIjoiaHR0cDovL2tleWNsb2FrLmtleWNsb2FrLnN2Yy5jbHVzdGVyLmxvY2FsOjgwODAvcmVhbG1zL21hc3RlciIsImF1ZCI6WyJQQVNDQUxfSU5URUxMSUdFTkNFIiwiTU9ORVQiLCJIT0xBQ1JBQ1kiLCJhY2NvdW50IiwiVklOQ0kiXSwic3ViIjoiOTk0ZjgzYzctMWY1ZS00MjhlLTllYzAtYjEwNjMxODUwNGEyIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiQk9MVFpNQU5OX0JPVCIsInNlc3Npb25fc3RhdGUiOiIyNzU1M2YxYS1kYTQwLTQwMmMtOWZiZS04MzM5YTI4ZjI1YjgiLCJuYW1lIjoiVGVuYW50IFRlbmFudCIsImdpdmVuX25hbWUiOiJUZW5hbnQiLCJmYW1pbHlfbmFtZSI6IlRlbmFudCIsInByZWZlcnJlZF91c2VybmFtZSI6InRlbmFudCIsImVtYWlsIjoiYWlkdGFhc0BnYWlhbnNvbHV0aW9ucy5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYWNyIjoiMSIsInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJkZWZhdWx0LXJvbGVzLW1hc3RlciIsIm9mZmxpbmVfYWNjZXNzIiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJCT0xUWk1BTk5fQk9UIjp7InJvbGVzIjpbIkJPTFRaTUFOTl9CT1RfVVNFUiJdfSwiUEFTQ0FMX0lOVEVMTElHRU5DRSI6eyJyb2xlcyI6WyJQQVNDQUxfSU5URUxMSUdFTkNFX1VTRVIiXX0sIk1PTkVUIjp7InJvbGVzIjpbIk1PTkVUX1VTRVIiXX0sIkhPTEFDUkFDWSI6eyJyb2xlcyI6WyJIT0xBQ1JBQ1lfVVNFUiJdfSwiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19LCJWSU5DSSI6eyJyb2xlcyI6WyJWSU5DSV9VU0VSIl19fSwic2NvcGUiOiJlbWFpbCBwcm9maWxlIiwic2lkIjoiMjc1NTNmMWEtZGE0MC00MDJjLTlmYmUtODMzOWEyOGYyNWI4IiwidGVuYW50SWQiOiI5OTRmODNjNy0xZjVlLTQyOGUtOWVjMC1iMTA2MzE4NTA0YTIifQ==.jDtcwSRyrquZDIEjR_f52eafMGE5P9fSedbw6wKtTDRbfEpn7b0ME8-jMS29p8kQCOjVkJUyoMFNxbpu2-XRvKUl2knFWe6fxnr2eJElGyJx-op_jtBXavhl-cNJm4lS1lpoxZs2HmTdSQMg5hYAiO4x8j9ogUol6VWagmADLGzY_Y3mBGLkh5grAYvIi8hPL9rmAQuk_t5JEBTCobhvU-q6XWoxNSxB35AhgHYfMutdauowzQEmoVy0-l3UiAoLG4-A95QD7Cw31ynuNRCEdrB_2NBTxm8pkBJEFJdrAH9y_Cd2bdTDj_70P5Y29nAe_qpxD__oqBMiMbDGxxK_LA",
}

# Fetch tenant data
response = requests.get(get_url, headers=headers)
tenant_data = response.json()

# Check if the 'content' key is present in the response
if 'content' not in tenant_data:
    print("Error: No tenant data found in the API response.")
    exit()

# Extract the list of tenants from the API response
tenants = tenant_data['content']

# Function to update tenant data based on matching id
def update_tenant(tenant, updated_info):
    # Update tenant's fields with Excel data
    tenant['address']['latitude'] = updated_info['lat']
    tenant['address']['longitude'] = updated_info['long']
    tenant['description'] = updated_info['description']
    tenant['name'] = updated_info['description']
    tenant['defaultCurrency'] = "SAR"

    # Update tenantType in platformDetails 66e2e76d83d08979e96cee34 66e32b51b1dbc9702f4048a6 66e32a6e83d08979e96cee35
    tenant['platformDetails']["66e2e76d83d08979e96cee34"] = [updated_info['tenantType']]
    tenant['platformDetails']["66e32b51b1dbc9702f4048a6"] = [updated_info['tenantType']]
    tenant['platformDetails']["66e32a6e83d08979e96cee35"] = [updated_info['tenantType']]

    return tenant

# List to store updated tenant data
updated_tenants = []

# Iterate through each row in the Excel sheet and match it with the tenants from the API response
for index, row in df.iterrows():
    tenant_id = row['Id']  # Excel sheet's tenant ID
    # Find tenant in API response by ID
    matching_tenant = next((tenant for tenant in tenants if tenant['id'] == tenant_id), None)

    if matching_tenant:
        print(f"Updating tenant: {tenant_id}")
        # Update tenant data
        updated_tenant = update_tenant(matching_tenant, row)
        updated_tenants.append(updated_tenant)
    else:
        print(f"No matching tenant found for ID: {tenant_id}")

# Write the updated tenants data to a JSON file
with open('updated_tenants.json', 'w') as json_file:
    json.dump(updated_tenants, json_file, indent=4)

print("All updates stored in 'updated_tenants.json'.")

import requests
import pandas as pd
import json

# API endpoint and headers
url = 'https://ig.gov-cloud.ai/hcy-web/v1.0/product/platform/filter?platformId=664afc3caf2dfa4e7eeda5db&productOffering=PRODUCT&size=200&page=0'
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI3Ny1NUVdFRTNHZE5adGlsWU5IYmpsa2dVSkpaWUJWVmN1UmFZdHl5ejFjIn0.eyJleHAiOjE3Mjc0NTM3MzcsImlhdCI6MTcyNzQxNzczNywianRpIjoiY2IzYWVhMDEtMzJmZi00MWI2LTg2ODAtYjcwNTM4MTUwMjU3IiwiaXNzIjoiaHR0cDovL2tleWNsb2FrLmtleWNsb2FrLnN2Yy5jbHVzdGVyLmxvY2FsOjgwODAvcmVhbG1zL21hc3RlciIsImF1ZCI6WyJQQVNDQUxfSU5URUxMSUdFTkNFIiwiWFBYLUNNUyIsImNkZmciLCJhY2NvdW50Il0sInN1YiI6IjdjMmEwY2M1LTY5ODgtNDk5OS04ZjZkLTQ4MjM2MzQ4MmVlZiIsInR5cCI6IkJlYXJlciIsImF6cCI6IkhPTEFDUkFDWSIsInNlc3Npb25fc3RhdGUiOiI4ZjBhNzJiYi1mNmU3LTRjMjctYTc1Zi05M2YzM2QxODkxNjMiLCJuYW1lIjoibW9iaXVzIG1vYml1cyIsImdpdmVuX25hbWUiOiJtb2JpdXMiLCJmYW1pbHlfbmFtZSI6Im1vYml1cyIsInByZWZlcnJlZF91c2VybmFtZSI6InBhc3N3b3JkX3RlbmFudF9tb2JpdXNAbW9iaXVzZHRhYXMuYWkiLCJlbWFpbCI6InBhc3N3b3JkX3RlbmFudF9tb2JpdXNAbW9iaXVzZHRhYXMuYWkiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYWNyIjoiMSIsImFsbG93ZWQtb3JpZ2lucyI6WyIvKiJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsiZGVmYXVsdC1yb2xlcy1tYXN0ZXIiLCJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiUEFTQ0FMX0lOVEVMTElHRU5DRSI6eyJyb2xlcyI6WyJTVVBFUkFETUlOIl19LCJYUFgtQ01TIjp7InJvbGVzIjpbIlhQWC1DTVNfVVNFUiJdfSwiSE9MQUNSQUNZIjp7InJvbGVzIjpbIkhPTEFDUkFDWV9VU0VSIl19LCJjZGZnIjp7InJvbGVzIjpbIkJPTFRaTUFOTl9CT1RfVVNFUiJdfSwiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJwcm9maWxlIGVtYWlsIiwic2lkIjoiOGYwYTcyYmItZjZlNy00YzI3LWE3NWYtOTNmMzNkMTg5MTYzIiwidGVuYW50SWQiOiI3YzJhMGNjNS02OTg4LTQ5OTktOGY2ZC00ODIzNjM0ODJlZWYiLCJyZXF1ZXN0ZXJUeXBlIjoiVEVOQU5UIn0=.SfwsT1ocTQwPPE7SszSgkwoZ60h_Pd96aq56br_AH-mQ3U2in-61cz1csYJgQl_PFf_SMAgHi-rccR8riIMp2UzhhNVSDcqm1-xyyZBIGF_QkJvL_46tbar3IDZmfMFhcRcssh4fQqv5rLLiOkz-avZ6nsxmCKHnvfvtcLHa_olfsByzkQug3FmaGgB8MkqQPLAaDyQGO5lGeSa-EIjayqjYtsGldXXLi67VPhxOxRPVEodo5MXV7kez83zn-0k-mBfOYu7emM25fMZe6A_nndwPHPAkSWFpsu0fiYgN1FvtYpOJRy_BR_EORBtc66fmJqUUlpBFFtPL_I-L0g4MFg'  # Placeholder for your token
}

# Send the request to the API
response = requests.get(url, headers=headers)

# Check if the response was successful
if response.status_code == 200:
    data = response.json()  # Parse the JSON response
    
    # Assuming the data contains a list of products in a key called 'content'
    if 'content' in data and data['content']:
        # Extract productId and masterConfigId and save in a new JSON file
        product_master_config = [
            {
                'productId': item['id'],
                'masterConfigId': item['productMasterConfigId']
            }
            for item in data['content'] if 'productMasterConfigId' in item
        ]
        
        # Save the productId and masterConfigId to a separate JSON file
        with open('productMasterConfig.json', 'w') as json_file:
            json.dump(product_master_config, json_file, indent=2)
        
        print("Data written to 'productMasterConfig.json'")
    else:
        print("No 'content' found in the API response or the content is empty.")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
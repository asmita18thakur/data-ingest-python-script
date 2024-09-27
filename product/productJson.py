import math
import pandas as pd
import json


# Load Excel data
df = pd.read_excel('newProducts.xlsx')
df.fillna(0,inplace=True)

# Convert to JSON
json_data = []
for index, row in df.iterrows():
   
    data = {
    "plan": {
        "rateCardIds": {},
    },
    "name": row['Product Name'],
    "platformId": "66f2dec4b1dbc9702f4049b7",
    "parentPlatformId": "664afc3caf2dfa4e7eeda5db",
    "description": row['Description'],
    "productType": row['Type'],
    "logoUrl": row['Logo'],
    "productTags": [
        "OTT",
        "DATA CASTING"
    ],
    "servingAreas": [],
    "snapshotsUrls": [],
    "attachedDocumentsUrls": [],
    "videoUrls": [],
    "videos": [],
    "allowsMultiplePurchases": False,
    "productRoles": [
        "ROLE_CONSUMER",
        "ROLE_USER",
        "ROLE_MARKETPLACE_USER"
    ],
    "config": {},
    "ownerId":"81befae9-1743-4aa5-ab5d-4b6e04bb5ada",
    "version": "v1.0",
    "hostedApps": [],
    "interestedTenants": [],
    "productStatus": "PENDING_AT_SU",
    "currency": "USD",
    "visibility": "PUBLIC",
    "participation": "OPEN",
    "listing": "PUBLIC",
    "vendorCommercials": [],
    "salesCount": 0,
    "vendorCount": 0,
    "schemaNodes": [],
    "universeNodes": [],
    "groupNodes": [],
    "contextNodes": [],
    "aqNodes": [],
    "templateNodes": [],
    "chartNodes": [],
    "baNodes": [],
    "engagementNodes": [],
    "wfNodes": [],
    "mappingNode": [],
    "metaData": {},
    "createdBy": "",
    "productOffering": "PRODUCT",
    "rating": 0.0,
    "commentCount": 0,
    "allianceCount": 0,
    "ratingCount": 0,
    "prices": [
        "AD_BASED",
        "Paid"
    ],
    "constructType": "BA",
    "constructId": "123",
    "enableAccessTokenIssuance": False,
    "enableIdTokenIssuance": False,
    "fallbackPublicClient": True
    }
    json_data.append(data)

# Write JSON data to a file
output_filename = 'product.json'
with open(output_filename, 'w') as json_file:
    json.dump(json_data, json_file, indent=4)

print(f"JSON data has been written to '{output_filename}'")
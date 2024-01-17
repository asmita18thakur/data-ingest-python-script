import math
import pandas as pd
import json


# Load Excel data
df = pd.read_excel('Holacracy Data Ingestion CES 2024.xlsx',sheet_name='Product')
df.fillna(0,inplace=True)

# Convert to JSON
json_data = []
for index, row in df.iterrows():
   
    data = {
    "name": row['name'],
    "platformId": row['platformId'] ,
     "plan": {
        "rateCardIds": {},
        "defaultRatecardId":"64c2762b0975f4693387bb96"
    },
    "description": row['description'] or "",
    "productType": row['productType'],
    "logoUrl": row['logoUrl'],
    "productTags": [
        "OTT",
        "DATA CASTING"
    ],
    "masterConfig": {},
    "servingAreas": [],
    "snapshotsUrls": [],
    "relatedInformation": row['relatedInformation'],
    "attachedDocumentsUrls": [],
    "videoUrls": [],
    "videos": [],
    "website": row['website'],
    "allowsMultiplePurchases": 'true',
    "productRoles": [
        "ROLE_CONSUMER",
        "ROLE_USER",
        "ROLE_MARKETPLACE_USER"
    ],
    "config": {},
    "ownerId": "64e1fd3d1443eb00018cc231",
    "productUrl": row['name'],
    "version": "v1.0",
    "hostedApps": [],
    
    "domain": "",
    "allianceInfo": {},
    "interestedTenants": [],
    "currency": "USD",
    "plpConfiguration": {},
    "participation": "OPEN",
    "tenantName": "",
    "alliancedProduct": "",
    "createdBy":row['createdBy'],
    "metaData":row["metaData"],
    "productOffering": "PRODUCT",
            "rating": 5.0,
            "prices": [
                "Paid",
                "AD_BASED"
    ]

}
    json_data.append(data)

# Write JSON data to a file
output_filename = 'product.json'
with open(output_filename, 'w') as json_file:
    json.dump(json_data, json_file, indent=4)

print(f"JSON data has been written to '{output_filename}'")
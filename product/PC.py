import math
import pandas as pd
import json


# Load Excel data
df = pd.read_excel('product_data.xlsx')
df.fillna(0,inplace=True)

# Convert to JSON
json_data = []
for index, row in df.iterrows():
   
    data = {
     "name": row['name'],
    "platformId": row['platformId'],
    "plan": {
        "rateCardIds": {},
        "defaultRatecardId": "64c2762b0975f4693387bb96"
    },
    "description": row['description'] or "",
    "productType": row['productType'],
    "logoUrl": row['logoUrl'],
    "productTags": [
        "OTT",
        "DATA CASTING"
    ],
    "masterConfig": {
        "REST Api Controller": {
            "children": {
                "Dynamic Rest Call Api": {
                    "apiType": "REST",
                    "communicationType": "SYNC",
                    "children": {
                        "HTTP-HEADERS": {
                            "children": {
                                "Content-Type": {
                                    "dataType": "STRING",
                                    "value": "application/json",
                                    "mandatory": False,
                                    "modificationAllowed": False,
                                    "type": "PROPERTY",
                                    "link": "",
                                    "comment": ""
                                },
                                "Accept": {
                                    "dataType": "STRING",
                                    "value": "/",
                                    "mandatory": False,
                                    "modificationAllowed": False,
                                    "type": "PROPERTY",
                                    "link": "",
                                    "comment": ""
                                }
                            },
                            "type": "GROUP"
                        },
                        "REQUEST-BODY": {
                            "children": {
                                "_$": {
                                    "dataType": "OBJECT",
                                    "value": "",
                                    "mandatory": False,
                                    "modificationAllowed": False,
                                    "type": "PROPERTY",
                                    "link": "",
                                    "comment": ""
                                }
                            },
                            "type": "GROUP"
                        },
                        "RESPONSE-BODY": {
                            "children": {
                                "_$": {
                                    "dataType": "OBJECT",
                                    "value": "",
                                    "mandatory": False,
                                    "modificationAllowed": False,
                                    "type": "PROPERTY",
                                    "link": "",
                                    "comment": ""
                                }
                            },
                            "type": "GROUP"
                        },
                        "HTTP-URL": {
                            "dataType": "STRING",
                            "value": "",
                            "mandatory": False,
                            "modificationAllowed": False,
                            "type": "PROPERTY",
                            "link": "",
                            "comment": ""
                        },
                        "HTTP-METHOD": {
                            "dataType": "STRING",
                            "value": "",
                            "mandatory": False,
                            "modificationAllowed": False,
                            "type": "PROPERTY",
                            "link": "",
                            "comment": ""
                        }
                    },
                    "type": "API"
                }
            },
            "type": "GROUP"
        }
    },
    "servingAreas": [],
    "snapshotsUrls": [],
    "relatedInformation": row['relatedInformation'] or "Dont know what sort of related information.",
    "attachedDocumentsUrls": [],
    "videoUrls": [],
    "videos": [],
    "website": row['website'] or "www.website.com",
    "allowsMultiplePurchases": True,  # Corrected to a boolean value
    "productRoles": [
        "ROLE_CONSUMER",
        "ROLE_USER",
        "ROLE_MARKETPLACE_USER"
    ],
    "config": {},
    "ownerId": "64e1fd3d1443eb00018cc231",
    "productUrl": row['productUrl'] or "www.google.com/product/url",
    "version": "v1.0",
    "hostedApps": [],
    "subscriptionStatus": "TRIAL",
    "domain": "",
    "allianceInfo": {},
    "interestedTenants": [],
    "currency": "USD",
    "plpConfiguration": {},
    "participation": "OPEN",
    "tenantName": "",
    "alliancedProduct": "",
    "productOffering": "PRODUCT",
    "constructType": "BA",  # Added field
    "constructId": "123",  # Added field
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
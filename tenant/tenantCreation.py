import pandas as pd
import json
import random
# Load Excel data
df = pd.read_excel('tenant.xlsx')

# Convert to JSON
json_data = []
for index, row in df.iterrows():
    data = {
        #  "id": row['id'],
         "countryCode": "+1",
         "description": " Tenant",
         "version": "v1.0",
         "url": 'www.'+str(row['userName'])+'.com',
         "emailId":row['email'],
        "organisationId": row['organisationId'],
        "dmas": [],
         "selectedTags": [],
        "telephoneNum": str(random.randint(1000000000, 9999999999)),
        "interestedProducts": [],
         "address": {
                "addressLine1": "",
                 "addressLine2": "",
                 "city": row['city'],
                 "state": "california",
                 "country": "USA",
                 "postCode": str(row['zipcode']),
                 "longitude": float(row['long']),
                 "latitude": float(row['lat']),
                 "type": "PRIMARY"
    },
    "defaultCurrency": "USD",
    "currenciesSupported": [],
    "logo": "www.mobius.com/images",
    "userName": str(row['userName'])+'@gatestautomation.com',
    "firstName": "Mobius",
    "lastName": "Gaian",
    "name": row['userName'],
    "password": "Gaian@123",
    "parentTenantId": row['parentTenantId'],
    "product":{
        row['product']:[
                "MARKETPLACE_USER"
    ]
    },
    "platformDetails":    {
        row['platformDetails']: [
            "AP","TP","XP","CP","IP"
        ]
    },
    "userType": "TENANT"
    
    }
    
    json_data.append(data)
    break

# Write JSON data to a file
output_filename = 'tenant.json'
with open(output_filename, 'w') as json_file:
    json.dump(json_data, json_file, indent=4)

print(f"JSON data has been written to '{output_filename}'")
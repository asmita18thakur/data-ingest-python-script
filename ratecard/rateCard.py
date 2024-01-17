import pandas as pd
import json

# Load Excel data
df = pd.read_excel('ratecard.xlsx')
df.fillna("",inplace=True)

# Convert to JSON
json_data = []
for index, row in df.iterrows():
    

    data = {
        "name": row['name'],
        "primaryRateCardId": "64c2762b0975f4693387bb96",
        "version": "v1.0",
        "platformId": row['platformId'],
        "rateCardType": row['rateCardType'],
        "paasFee": {
            "description": "",
            "fixedFee": row['paas'],
            "type": "PAAS",
            "queryId": "5555",
            "multiplierField": "null",
            "baseFee": 0.0,
            "validityFrom": 1665413598.391,
            "validityTo": 1731196800.0,
            "unit": "MONTHS"
        },
        "saasFee": {
            "description": "",
            "fixedFee": row['saas'],
            "type": "SAAS",
            "queryId": "55555",
            "multiplierField": "null",
            "baseFee": 0.0,
            "validityFrom": 1665413598.391,
            "validityTo": 1731196800.0,
            "unit": "MONTHS"
        },
        "apiCountFee": {
            "description": "",
            "fixedFee": row['apicount'],
            "type": "COUNT",
            "queryId": "5555",
            "multiplierField": "null",
            "baseFee": 70.0,
            "validityFrom": 1646765091.204,
            "validityTo": 1646765091.204,
            "unit": "MINUTES"
        },
        "volCountFee": {
            "description": "",
            "fixedFee": row['volCount'],
            "type": "VOLUME",
            "queryId": "5555",
            "multiplierField": "null",
            "baseFee": 90.0,
            "validityFrom": 1646765091.204,
            "validityTo": 1646765091.204,
            "unit": "MINUTES"
        },
        "adFee": {
            "description": "",
            "fixedFee": row['Adfee'],
            "type": "AD",
            "queryId": "5555",
            "multiplierField": "null",
            "baseFee": 80.0,
            "validityFrom": 1646765091.204,
            "validityTo": 1646765091.204,
            "unit": "MINUTES"
        },
        "adRevenueShare": {
            "description": "",
            "fixedShare": row['adRevenueShare'],
            "revenueShareType": "AD",
            "queryId": "55555",
            "multiplierField": "null",
            "baseShare": 0.0,
            "eligibleForRoyalty": False
        },
        "consumerRevenueShare": {
            "description": "",
            "fixedShare": row['consumerRevenueShare'],
            "revenueShareType": "AD",
            "queryId": "5555",
            "multiplierField": "null",
            "baseShare": 0.0,
            "eligibleForRoyalty": False
        },
        "dataSharable": True,
        "currency": "INR",
        "isActive": True,
        "contextId": "5555",
        "keywords": [],
        "billingCycleUnit": "MINUTES",
        "billingCycle": 2,
        "eligibleForRoyalty": True,
        "comment": "Comment Section.",
        "defaultRateCard": False
    }

    json_data.append(json.dumps(data, indent=4))  # Convert dictionary to JSON string

# Add 'json' column to DataFrame
df['json'] = json_data

# Write updated DataFrame back to the same Excel file
df.to_excel('ratecard.xlsx', index=False)

print("JSON data has been added to the 'json' column in 'ratecard.xlsx'")
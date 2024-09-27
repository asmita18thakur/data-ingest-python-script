import pandas as pd
import json
import datetime


# Load Excel data
df = pd.read_excel('ratecards.xlsx')
df.fillna("",inplace=True)

# Get today's date in UNIX timestamp format
today = datetime.datetime.now().timestamp()

# Calculate 'validityTo' as 3 years from today
three_years = datetime.timedelta(days=3*365)  # Consider 365 days per year for simplicity
validity_to = (datetime.datetime.now() + three_years).timestamp()

# Convert to JSON
json_data = []
for index, row in df.iterrows():
    # Generate a unique name and description for each payload

    # Create the payload
    data = {
        "name": row['Rate Card Name'],
        "description": row['Description'],
        "platformId": "66f2dec4b1dbc9702f4049b7",
        "rateCardType": row['Rate Card Type'],
        "paasFee": {
            "fixedFee": row['paas'],
            "baseFee": "0.0",
            "validityFrom": today,
            "validityTo": validity_to
        },
        "saasFee": {
            "fixedFee": row['saas'],
            "validityFrom": today,
            "validityTo": validity_to
        },
        "apiCountFee": {
            "validityFrom": today,
            "validityTo": validity_to,
            "perApiFee": row["apicount"],
            "apiLimit": 25,
            "baseFee": 12
        },
        "dataVolumeFee": {
            "validityFrom": today,
            "validityTo": validity_to,
            "perVolumeFee": 122.5,
            "volumeLimit": 25,
            "fixedFee": row['volCount'],
            "dataUnitType": "BYTE"
        },
        "currency": "INR",
        "isActive": True,
        "contextId": "Context_Id",  # You can replace this with actual context ID if available
        "billingCycleUnit": "MINUTES",
        "billingCycle": "2",
        "eligibleForRoyalty": True,
        "comment": "Comment Section.",
        "rateCardFor": "PRODUCT"
    }

    # Append the JSON string to the list
    json_data.append(json.dumps(data, indent=4))

# Add the JSON data to a new column in the DataFrame
df['json'] = json_data

# Write updated DataFrame back to the same Excel file
df.to_excel('ratecards.xlsx', index=False)

print("JSON data has been added to the 'json' column in 'ratecards.xlsx'")
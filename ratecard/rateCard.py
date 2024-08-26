import pandas as pd
import json
import datetime


# Load Excel data
df = pd.read_excel('rate_card.xlsx')
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
    name = f"Ratecard_{row['name']}"
    description = f"Ratecard description for {name}"

    # Create the payload
    data = {
        "name": row['name'],
        "description": description,
        "platformId": row['platformId'],
        "rateCardType": row['rateCardType'],
        "paasFee": {
            "fixedFee": row['paasFee_fixedFee'],
            "baseFee": "0.0",
            "validityFrom": today,
            "validityTo": validity_to
        },
        "saasFee": {
            "fixedFee": row['saasFee_fixedFee'],
            "validityFrom": today,
            "validityTo": validity_to
        },
        "apiCountFee": {
            "validityFrom": today,
            "validityTo": validity_to,
            "perApiFee": 122.5,
            "apiLimit": 25,
            "baseFee": 12
        },
        "dataVolumeFee": {
            "validityFrom": today,
            "validityTo": validity_to,
            "perVolumeFee": 122.5,
            "volumeLimit": 25,
            "fixedFee": row['dataVolumeFee_fixedFee'],
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

    # # Append the JSON string to the list
    json_data.append(json.dumps(data, indent=4))

    # Write JSON data to a file
output_filename = 'ratecard.json'
with open(output_filename, 'w') as json_file:
    json.dump(json_data, json_file, indent=4)

print(f"JSON data has been written to '{output_filename}'")

# Add the JSON data to a new column in the DataFrame
df['json'] = json_data

# Write updated DataFrame back to the same Excel file
df.to_excel('rate_card.xlsx', index=False)

print("JSON data has been added to the 'json' column in 'ratecards.xlsx'")
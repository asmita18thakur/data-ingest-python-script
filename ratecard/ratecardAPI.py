import json
import requests
import pandas as pd
import ast

# ============================


def is_valid_json(data):
    try:
        json.loads(data)
        return True
    except ValueError:
        return False

# Test examples
json_data = '{"name": "John", "age": 30, "city": "New York"}'
non_json_data = 'This is not JSON'


# =================================




# Load Excel data
df = pd.read_excel('ratecard.xlsx')



# Headers including Authorization token
headers = {
    'Content-Type': 'application/json',
  
}

responses = []
ratecard_ids = []
# Iterate over each payload
for index, row in df.iterrows():
    print(row['productID'])

    # API endpoint
    url = 'https://ig.aidtaas.com/market-place/v1.0/rate-cards/product/'+ str(row['productID'])
    print(url)
    try:
        json_payload = json.loads(row['json'])
    except json.JSONDecodeError:
        try:
            json_payload = ast.literal_eval(row['json'])
        except (SyntaxError, ValueError):
            print(f"Malformed JSON at index {index}: {row['json']}")
            responses.append("error")
            ratecard_ids.append("error")
            continue  # Move to the next iteration
    
    response = requests.post(url, json=json_payload, headers=headers)
    response_json = response.json()
    responses.append(response_json)
    
    if response.status_code == 201:
        ratecard_ids.append(response_json.get('id', ''))
        # print("Successfully created:", response_json)
    else:
        ratecard_ids.append("error")
        print("Error response:", response.status_code, response_json)


# Save responses to a file
with open('rateCardResponse.json', 'w') as responses_file:
    json.dump(responses, responses_file, indent=4)

print("Responses saved successfully.")

# Add 'AccountID' column to DataFrame
df['RateCardID'] = ratecard_ids

# Write updated DataFrame back to the same Excel file
df.to_excel('ratecard.xlsx', index=False)

print("Excel file updated with ratecardIDS")


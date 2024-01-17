import json
import requests
import pandas as pd

token = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImZmOGYxNjhmLTNmZjYtNDZlMi1iMTJlLWE2YTdlN2Y2YTY5MCJ9.eyJwcm9maWxlVXJsIjoiaHR0cHM6Ly9kZXYtcGkuZ2FpYW5zb2x1dGlvbnMuY29tLyIsInJlY2VudF9zZXNzaW9uIjoiTkEiLCJzdWIiOiJnYWlhbi5jb20iLCJwYXJlbnRUZW5hbnRJZCI6Ik5BIiwiY29sb3IiOiJibGFjayIsInVzZXJfbmFtZSI6InNpbXJhbi5sYWxsQGdhdGVzdGF1dG9tYXRpb24uY29tIiwiaXNzIjoiZ2FpYW4uY29tIiwiaXNBZG1pbiI6dHJ1ZSwicGxhdGZvcm1JZCI6IjY1NGJhZTZkN2ViOTA0MDNmYjhhMTQ5NyIsInVzZXJOYW1lIjoic2ltcmFuLmxhbGxAZ2F0ZXN0YXV0b21hdGlvbi5jb20iLCJhdXRob3JpdGllcyI6WyJST0xFX01BUktFVFBMQUNFX1VTRVIiXSwiY2xpZW50X2lkIjoiZ2FpYW4iLCJzY29wZSI6WyJ0cnVzdCIsInJlYWQiLCJ3cml0ZSJdLCJ0ZW5hbnRJZCI6IjY1N2E4OWRhNDc1YTk3MDAwMWQyMjlkMiIsImxvZ28iOiJodHRwOi8vaWcuZ2FpYW5zb2x1dGlvbnMuY29tL2NvbnRlbnQtc2VydmljZS92MS4wL2NvbnRlbnQvZG93bmxvYWQvZWY4MmRiMjAtOTg3ZC00Zjg2LWIyY2YtMDdmMzE5NzE3MDVjIiwiZXhwIjoxNzA0OTkwMjg2LCJqdGkiOiJiNmU4MjkyMy1kMDNjLTQzY2ItYjc3MS1iNDNkZTU0NDhiYWMiLCJlbWFpbCI6InNpbXJhbi5sYWxsQGdhdGVzdGF1dG9tYXRpb24uY29tIn0.lTPX202bvtg0zxzl5jgL_LFzcjmf6T2WkspR-gmNi99gf4kqrTT2xI0x6p0I3ieMO27TTRk_0Y2mUv-pBhbLfSiT-0DssiQt4AvgM0dxnNPsGu5olZDJWQKjLt-Wgag0KSJjDhiiJz5Ux9BcPO1eG5WBkvorfVSq2U6RlvQ4Tyjwh5Bz3U4x7tDZ7YL7gpqMNh95NKHXODjf4SPG4oRHKU46xP-cs-mD8eLFPpN4bhVgBWXHedLBchOKhNN5QQAtX2116DsouPGGW-r3zlGPQhs-7iqjHi8lcDM6xfjBxNqwrjC_M_OTOEoAKnCGOyB6aVBgJ2vVLMPgt5GoT2dLqQ'


# # Load payloads from test.json
with open('product.json', 'r') as json_file:
    payloads = json.load(json_file)

# Load Excel data
df = pd.read_excel('productCreation.xlsx')


# API endpoint
url = 'https://ig.aidtaas.com/market-place/v1.0/products'

# Headers including Authorization token
headers = {
    'Content-Type': 'application/json',
    'Authorization': token
}

responses = []
product_ids = []

# Iterate over each payload
for payload in payloads:
    try:
        # Make a POST request
        response = requests.post(url, json=payload, headers=headers)
        
        # Get the response status code and text
        response_status = response.status_code
        response_text = response.text
        
        # Check if the response status is 200 (OK)
        if response_status == 201:
            try:
                # Try to parse the response as JSON
                response_json = response.json()
                responses.append(response_json)
                product_ids.append(response_json['id'])
            except json.JSONDecodeError:
                # If response is not valid JSON
                responses.append(response_text)
                product_ids.append(response_text)
                print(f"Response is not valid JSON: {response_text}")
        else:
            # If response status is not 200, print error message
            responses.append(response_text)
            product_ids.append(response_text)
            print(f"Request failed with status code {response_status}: {response_text}")

    except requests.RequestException as e:
        # If request itself fails (e.g., network error)
        responses.append(e)
        product_ids.append(e)
        print(f"Request failed: {e}")

# Save responses to a file
with open('productResponse.json', 'w') as responses_file:
    json.dump(responses, responses_file, indent=4)

print("Responses saved successfully.")
print(product_ids)

# Add 'AccountID' column to DataFrame
df['productID'] = product_ids

# Write updated DataFrame back to the same Excel file
df.to_excel('productCreation.xlsx', index=False)

print("Excel file updated with productIDs.")

import pandas as pd
import requests
import math
import json

# Load the Excel files
tenant_file = pd.read_excel('tenant.xlsx')  # Assuming 'tenant_a.xlsx' has Tenant A details

# Load the Excel file
# file_path = 'negotiation.xlsx'  # Path to your Excel file
df = pd.read_excel(tenant_file)

# URL of the API endpoint
url = 'https://ig.gov-cloud.ai/hcy-web/v1.0/negotiations'
payloads = []

# Iterate over each row in the DataFrame    
response_ids = []
for index, row in df.iterrows():
    payload = {
        "sellerId": row['sellerId'],
        "productId": row['productId'],
        "rateCardId": row['rateCardId'],
        "productNegotiationRateCardId": row['negotiationRateCardId'],
        "negotiationRateCardPlanType": row['planType'],
        "buyerId": row['buyerId'],
        "appId": row['appId'],
        "platformId": row['platformId'],
        "negotiatedBy": row['negotiatedBy']
        }
    

    payloads.append(payload)

    with open('negotiation.json', 'w') as json_file:
        json.dump(payload, json_file, indent=4)

    # Send the POST request
    headers = {
        'Content-Type': 'application/json',
        'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImZmOGYxNjhmLTNmZjYtNDZlMi1iMTJlLWE2YTdlN2Y2YTY5MCJ9.eyJzdWIiOiJnYWlhbi5jb20iLCJ1c2VyX25hbWUiOiJwb3J0YWxfdGVzdCIsInNjb3BlIjpbInRydXN0IiwicmVhZCIsIndyaXRlIl0sInRlbmFudElkIjoiNjExYmRkMzQyNmE5NDg2MDA1NjkzYjExIiwiaXNzIjoiZ2FpYW4uY29tIiwidXNlck5hbWUiOiJwb3J0YWxfdGVzdCIsImF1dGhvcml0aWVzIjpbIlJPTEVfT01OSV9DT05TVU1FUiIsIlJPTEVfTUFSS0VUUExBQ0VfVVNFUiIsIlJPTEVfT01OSV9VU0VSIl0sImp0aSI6IjgxODE1ZDNmLTY1MTAtNDJkNC05NWZkLTNiZTJmMWYzYjg5ZiIsImVtYWlsIjoicG9ydGFsX3Rlc3RAZ2F0ZXN0YXV0b21hdGlvbi5jb20iLCJjbGllbnRfaWQiOiJnYWlhbiJ9.Mz1gWLt1rujlQWW3SzuwtERk1i6HwG9utVuMUnL-RX4kKtR1jl0eR9MZmNjRZ0znbrr6w8MOj2aAULtpIEYmM9jU_mXGBuqetPIbTuV2d4Hkv6f0qaJZLAIAU3qhgijQI9O4a2yg_rmHnibNhEcZMKEFK5AXw8M_B8XIgnNYlXDkpjEqP6Siv0HJmHA3T1j1XY8PCsluzIwDzIgRr-xqAJcaCnUwGR7XxsF-X0plk8L9qV1Z3bF2EMqqBsednYeqaM3EqwJXk27R5PFU7jn5aOc-_n9DxaGLcuJB5JoqoGW7DeaIKLzMwxvS9vP_bc8vDOxl8xk-zTRAq8goyHV6IQ'
    }
    response = requests.post(url, json=payload, headers=headers)
    response_json = response.json()
    # Store the response ID or an error message
    if response.status_code == 200:
        response_id = response_json.get('id', 'No ID in response')
        response_ids.append(response_id)
    else:
        response_ids.append(f"Error: {response.status_code}")
        print(response_json)

# Add the response IDs to the DataFrame
df['response_id'] = response_ids

with open('negotiationResponse.json', 'w') as json_file:
    json.dump(payloads, json_file, indent=4)

# Save the DataFrame back to the Excel file
df.to_excel(file_path, index=False)

print("Script completed. Response IDs have been written to the Excel file.")

import json
import requests
import pandas as pd

# Read JSON data directly from the file
with open('walletCard.json', 'r') as file:
    data = json.load(file)

def send_comment_to_api(comment_data):
    """Send comment data to the API and handle the response."""
    url = 'https://ig.gov-cloud.ai/mobius-payment-service/v1.0/card-details'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6InEtMjNmYWxldlpoaEQzaG05Q1Fia1A1TVF5VSJ9.eyJhdWQiOiJhNWI4ODBiNC01N2IxLTQyODktOWRiYS1hNjA5NDA1ZGY4ZGYiLCJpc3MiOiJodHRwczovL2xvZ2luLm1pY3Jvc29mdG9ubGluZS5jb20vY2ZkYzkxMGQtMzVkMC00YjQxLWE1YmMtNmU3MDdiYWE3ZGJiL3YyLjAiLCJpYXQiOjE3MTE4MTk4NzMsIm5iZiI6MTcxMTgxOTg3MywiZXhwIjoxNzExODI0MTQyLCJhaW8iOiJBVVFBdS84V0FBQUFvall4QWxNamxpbUpZUkk4ZmFvMmM1QjhSME9kTTRNNGFzQ3dRSC90RXUwU2FSTnIzMmtlWmthNTZ6dmRpOTZleFRNQ0p4Y3pPNUxlQUdTeFZIS3V3QT09IiwiYXpwIjoiYTViODgwYjQtNTdiMS00Mjg5LTlkYmEtYTYwOTQwNWRmOGRmIiwiYXpwYWNyIjoiMCIsIm5hbWUiOiJ0ZXN0IHVzZXIzIiwib2lkIjoiNjgxMDVmM2MtNjZjNi00ZWNhLTkxZTItYzNlY2Y5MGI2MThiIiwicHJlZmVycmVkX3VzZXJuYW1lIjoiamF5ZXNoLm1hbGF2aXlhX2dhaWFuc29sdXRpb25zLmNvbUBnYWlhdHYuaW4iLCJyaCI6IjAuQVNvQURaSGN6OUExUVV1bHZHNXdlNnA5dTdTQXVLV3hWNGxDbmJxbUNVQmQtTjhxQVA0LiIsInJvbGVzIjpbIkVYRUNVVEUiLCJXUklURSIsIlJFQUQiXSwic2NwIjoiU0NPUEUiLCJzdWIiOiJRM25GRVZKSUo4cFdqZXhVa3k0aFpyLU93bS10dTNRNVVBOXR4d3VDVTdzIiwidGlkIjoiY2ZkYzkxMGQtMzVkMC00YjQxLWE1YmMtNmU3MDdiYWE3ZGJiIiwidXRpIjoiWnBVV3g2RXlla2VGZ0lkZnctMG9BQSIsInZlciI6IjIuMCIsInRlbmFudElkIjoiNjgxMDVmM2MtNjZjNi00ZWNhLTkxZTItYzNlY2Y5MGI2MThiIn0.HJ6Ygs8Xa7oDHqFcEZuj5CgdVpsAE2sGdCgL-sjvC7Ku8WHsmFNakoNjrXB_UaDXRJXSE_B3jL5XhVxpztelFb3gOK-BQss-s1HzmCFstxrpjkKdySMIZc_-ifHBBed85L0NkwYEH40GBZNEYAVwF4r41pIanqDUS9H7oH3jevErmnvRUEx2xBfnwhSY14KCPoDwkgZ0y9jKhrHL2NmkswMAIAyD74W0BQ4q2NJNj0xWhp_vO8vH0TLM8e6nUBdfKddcQIidYf_QTVaj9aizs9xz9Y4zys2-KzQmRK5QpapWxgHfjfEMJ6DfyVBnRL-c2XvC_FCmi_BTrA28uXksbA'  # Replace [Your_Access_Token] with your actual access token
    }
    try:
        response = requests.post(url, json=data, headers=headers)
        print("Sending data to API:", comment_data)  
        response.raise_for_status()  # Will raise an exception for HTTP codes 400 or 500
        return response
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - {response.text}")  # Python 3.6+
    except Exception as err:
        print(f"An error occurred: {err}")

# Extract the comment part from the data for the API request
comment_data = data  # Adjust this if the data structure is different

# Send the comment data to the API
response = send_comment_to_api(comment_data)
if response:
    response_data = {
        'Status Code': response.status_code,
        'Response': response.json() if response.status_code == 200 else response.text
    }

    # Save the response to a JSON file
    with open('walletCardAPI_response.json', 'w') as outfile:
        json.dump(response_data, outfile, indent=4)

    # Convert the response data to a DataFrame and save as Excel
    df = pd.DataFrame([response_data])
    df.to_excel('walletCardAPI_response.xlsx', index=False)

    print("Response saved successfully in JSON and Excel formats.")
else:
    print("Failed to receive a valid response from the API.")

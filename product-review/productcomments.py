import json
import requests
import pandas as pd

# Read JSON data directly from the file
with open('product_comments.json', 'r') as file:
    data = json.load(file)

def send_comment_to_api(comment_data):
    """Send comment data to the API and handle the response."""
    url = 'https://ig.gov-cloud.ai/hcy-web/v1.0/product/comment'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI3Ny1NUVdFRTNHZE5adGlsWU5IYmpsa2dVSkpaWUJWVmN1UmFZdHl5ejFjIn0.eyJleHAiOjE3MjQ5NDczMjUsImlhdCI6MTcyNDkxMTMyNSwianRpIjoiNDMzNDQ2NDQtNjQ5Mi00N2M3LTllMTItZTg1YWJmYjdlOGUwIiwiaXNzIjoiaHR0cDovL2tleWNsb2FrLmtleWNsb2FrLnN2Yy5jbHVzdGVyLmxvY2FsOjgwODAvcmVhbG1zL21hc3RlciIsImF1ZCI6ImFjY291bnQiLCJzdWIiOiJiYjI4Y2FlNS05YjY4LTQ0ZDgtYmFlMy0wMzJhYTM2MmE1ZDMiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJIT0xBQ1JBQ1kiLCJzZXNzaW9uX3N0YXRlIjoiMzQ5MjI4MDItMmRiMS00YmYwLTg2NzAtYzZiNDg3NjZkMWZkIiwibmFtZSI6InZveGEuY29tIHZveGEiLCJnaXZlbl9uYW1lIjoidm94YS5jb20iLCJmYW1pbHlfbmFtZSI6InZveGEiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJwYXNzd29yZF90ZW5hbnRfdm94YUBnbWFpbC5jb20iLCJlbWFpbCI6InBhc3N3b3JkX3RlbmFudF92b3hhQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbIi8qIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJkZWZhdWx0LXJvbGVzLW1hc3RlciIsIm9mZmxpbmVfYWNjZXNzIiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJIT0xBQ1JBQ1kiOnsicm9sZXMiOlsiSE9MQUNSQUNZX1VTRVIiXX0sImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoicHJvZmlsZSBlbWFpbCIsInNpZCI6IjM0OTIyODAyLTJkYjEtNGJmMC04NjcwLWM2YjQ4NzY2ZDFmZCIsInRlbmFudElkIjoiYmIyOGNhZTUtOWI2OC00NGQ4LWJhZTMtMDMyYWEzNjJhNWQzIiwicmVxdWVzdGVyVHlwZSI6IlRFTkFOVCJ9.Vk0sTgAPeE4kV_Oefo34HcfylUN8cq9jBsgvDdwtF99ZOChfXmlSyWusg79lmU6PV2Y3EPfl4sR-AWGR-SmrX7Rfi8cWv_zFGnUrOoqf6be9JKyHcEMjsCpLPIC0jPSbo2CXR6Jq3pYFUusB6o9JXI7JiZUsxgfAG4xRc-0lx5_2sl8tCgziqz5pYfTBFsmVy64o5_B67CGwIzwhBoqqNMzEKsY54EWpeaM-KPp0zHvlJF_6H-0LDwDuuTHbOK24DXNU3Oc_Z-DnM1QBuIa2bX2nWDWaiRTaxmSEYrzcMfwdgATRWGzyPovcZxDBLxToaJJ9QNwE9ENg5addo7PFnA'  # Replace [Your_Access_Token] with your actual access token
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
comment_data = data['comments']  # Adjust this if the data structure is different

# Send the comment data to the API
response = send_comment_to_api(comment_data)
if response:
    response_data = {
        'Status Code': response.status_code,
        'Response': response.json() if response.status_code == 200 else response.text
    }

    # Save the response to a JSON file
    with open('api_response.json', 'w') as outfile:
        json.dump(response_data, outfile, indent=4)

    # Convert the response data to a DataFrame and save as Excel
    df = pd.DataFrame([response_data])
    df.to_excel('api_response.xlsx', index=False)

    print("Response saved successfully in JSON and Excel formats.")
else:
    print("Failed to receive a valid response from the API.")

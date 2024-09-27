import os
import http.client
from codecs import encode
import json

def upload_image(file_path, file_name, token):
    conn = http.client.HTTPSConnection("ig.gov-cloud.ai")

    # Specify the CDN upload URL
    upload_url = '/mobius-content-service/v1.0/content/upload?filePathAccess=private&filePath=%2Fingestion'

    # Specify the headers, including the authorization token
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryvY13FvRix6AYKfSm',
        'Accept': 'application/json, text/plain, */*',
    }

    # Create the multipart/form-data payload
    boundary = '----WebKitFormBoundaryvY13FvRix6AYKfSm'
    dataList = []

    # Content-Disposition header for the file
    dataList.append(encode(f'--{boundary}'))
    dataList.append(encode(f'Content-Disposition: form-data; name="file"; filename="{file_name}"'))
    dataList.append(encode('Content-Type: image/png'))  # Adjust the content type as needed
    dataList.append(encode(''))  # Empty line before the file data

    # Read the file content and add it to the payload
    with open(file_path, 'rb') as f:
        dataList.append(f.read())

    # End of the payload
    dataList.append(encode(f'--{boundary}--'))
    dataList.append(encode(''))

    body = b'\r\n'.join(dataList)

    # Make the HTTP request
    conn.request("POST", upload_url, body, headers)

    # Get the response
    res = conn.getresponse()
    data = res.read().decode("utf-8")

    # Parse the response JSON to extract the CDN URL
    response_json = json.loads(data)

    cdn_url = "https://cdn.gov-cloud.ai/"+response_json['cdnUrl']
    print(cdn_url)

    # Close the connection
    conn.close()

    return cdn_url

def main():
    # Set the folder path containing the images
    folder_path = 'logourl-2/'

    # Specify the authorization token
    token = 'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI3Ny1NUVdFRTNHZE5adGlsWU5IYmpsa2dVSkpaWUJWVmN1UmFZdHl5ejFjIn0.eyJleHAiOjE3MjcyMjA0OTIsImlhdCI6MTcyNzE4NDQ5MiwianRpIjoiYzA2MTRmMGYtNzE1NC00NmQxLWExN2YtOTlkNzJlZTNkZGM2IiwiaXNzIjoiaHR0cDovL2tleWNsb2FrLmtleWNsb2FrLnN2Yy5jbHVzdGVyLmxvY2FsOjgwODAvcmVhbG1zL21hc3RlciIsImF1ZCI6WyJQQVNDQUxfSU5URUxMSUdFTkNFIiwiWFBYLUNMUyIsImNkZmciLCJhY2NvdW50Il0sInN1YiI6IjdjMmEwY2M1LTY5ODgtNDk5OS04ZjZkLTQ4MjM2MzQ4MmVlZiIsInR5cCI6IkJlYXJlciIsImF6cCI6IkhPTEFDUkFDWSIsInNlc3Npb25fc3RhdGUiOiJiNTA3OTNjNi1lMmU0LTQ5ZjgtOWZhMi00ODhlOWYzYjAyMDgiLCJuYW1lIjoibW9iaXVzIG1vYml1cyIsImdpdmVuX25hbWUiOiJtb2JpdXMiLCJmYW1pbHlfbmFtZSI6Im1vYml1cyIsInByZWZlcnJlZF91c2VybmFtZSI6InBhc3N3b3JkX3RlbmFudF9tb2JpdXNAbW9iaXVzZHRhYXMuYWkiLCJlbWFpbCI6InBhc3N3b3JkX3RlbmFudF9tb2JpdXNAbW9iaXVzZHRhYXMuYWkiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYWNyIjoiMSIsImFsbG93ZWQtb3JpZ2lucyI6WyIvKiJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsiZGVmYXVsdC1yb2xlcy1tYXN0ZXIiLCJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiUEFTQ0FMX0lOVEVMTElHRU5DRSI6eyJyb2xlcyI6WyJTVVBFUkFETUlOIl19LCJYUFgtQ01TIjp7InJvbGVzIjpbIlhQWC1DTVNfVVNFUiJdfSwiSE9MQUNSQUNZIjp7InJvbGVzIjpbIkhPTEFDUkFDWV9VU0VSIl19LCJjZGZnIjp7InJvbGVzIjpbIkJPTFRaTUFOTl9CT1RfVVNFUiJdfSwiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJwcm9maWxlIGVtYWlsIiwic2lkIjoiYjUwNzkzYzYtZTJlNC00OWY4LTlmYTItNDg4ZTlmM2IwMjA4IiwidGVuYW50SWQiOiI3YzJhMGNjNS02OTg4LTQ5OTktOGY2ZC00ODIzNjM0ODJlZWYiLCJyZXF1ZXN0ZXJUeXBlIjoiVEVOQU5UIn0=.M4zY10BpCK2VNxRCtvRGhOjK_0hEie_BNOfzlbHezmT976--ZGGmv9KIdvhlQjjS_clsFhEF2PWDcrREskfDARUU_BlPPdku6O-6DRdsckQ_LdBMhoj0Vfh-xPB61dtRxNhLyby1gK7knPUsRZ1LfLcz_B8Zt_nbrnHk7Y7bNf6-NyxtclDrTZPS_oKFVOo0ybKqM17qIhbxs3z-0rHop3wPdCvL7gvkDtDoiP-OD6zPcUXwo-gNsJVkvU2f0RNLOtq0xcIeN4E97FrHGaGM_Y5_6qZUXuOW5EwCa7VSMOoGFRs6c_zY8vnou6cDgcP97VddewR_OsdBO7TddH8vLQ'

    # Create a dictionary to store image names and corresponding CDN URLs
    image_data_dict = {}

    # Iterate through each file in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
       
        # Upload the image and get the CDN URL
        cdn_url = upload_image(file_path, filename, token)

        # Store the image name and CDN URL in the dictionary
        image_data_dict[filename] = cdn_url

    # Write the dictionary to a JSON file
    json_file_path = 'logourl-2/logoCDN.json'
    with open(json_file_path, 'w') as json_file:
        json.dump(image_data_dict, json_file, indent=2)

    print(f"CDN URLs written to {json_file_path}")

if __name__ == "__main__":
    main()

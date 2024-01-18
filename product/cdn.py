import os
import http.client
from codecs import encode
import json

def upload_image(file_path, file_name, headers, boundary):
    conn = http.client.HTTPSConnection("ig.aidtaas.com")

    # Specify the CDN upload URL
    upload_url = '/content-service/v1.0/content/upload/1154/64e1fd3d1443eb00018cc231/1154?overrideFile=true'

    # Create the multipart/form-data payload
    dataList = []

    # Content-Disposition header for each file
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name="file"; filename="{0}"'.format(file_name)))
    dataList.append(encode('Content-Type: application/octet-stream'))  # Adjust the content type as needed
    dataList.append(encode(''))

    # Read the file content and add it to the payload
    with open(file_path, 'rb') as f:
        dataList.append(f.read())

    # End of the payload
    dataList.append(encode('--' + boundary + '--'))
    dataList.append(encode(''))

    body = b'\r\n'.join(dataList)

    # Make the HTTP request
    conn.request("POST", upload_url, body, headers)

    # Get the response
    res = conn.getresponse()
    data = res.read().decode("utf-8")

    # Parse the response JSON to extract the CDN URL
    response_json = json.loads(data)
    cdn_url = response_json['url']

    # Close the connection
    conn.close()

    return cdn_url

def main():
    # Set the folder path containing the images
    folder_path = 'logourl/'

    # Specify the boundary for multipart/form-data
    boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'

    # Specify the headers
    headers = {
        'authority': 'ig.aidtaas.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImZmOGYxNjhmLTNmZjYtNDZlMi1iMTJlLWE2YTdlN2Y2YTY5MCJ9.eyJwcm9maWxlVXJsIjoid3d3Lmdvb2dsZS5jb20vcHJvZmlsZS9waWMiLCJyZWNlbnRfc2Vzc2lvbiI6Ik5BIiwic3ViIjoiZ2FpYW4uY29tIiwicGFyZW50VGVuYW50SWQiOiJOQSIsImNvbG9yIjoiYmxhY2siLCJ1c2VyX25hbWUiOiJ0ZW5hbnRfdWprc2VybmFtZSIsImlzcyI6ImdhaWFuLmNvbSIsImlzQWRtaW4iOnRydWUsInBsYXRmb3JtSWQiOiI2NTRiYWU2ZDdlYjkwNDAzZmI4YTE0OTciLCJ1c2VyTmFtZSI6InRlbmFudF91amtzZXJuYW1lIiwiYXV0aG9yaXRpZXMiOlsiUk9MRV9NQVJLRVRQTEFDRV9VU0VSIl0sImNsaWVudF9pZCI6ImdhaWFuIiwic2NvcGUiOlsidHJ1c3QiLCJyZWFkIiwid3JpdGUiXSwidGVuYW50SWQiOiI2NGUxZmQzZDE0NDNlYjAwMDE4Y2MyMzEiLCJsb2dvIjoid3d3Lmdvb2dsZS5jb20vdGVuYW50L2xvZ28ucG5nIiwiZXhwIjoxNzA0ODE4NjA0LCJqdGkiOiJmMGU5ZDQyMC1kNmE1LTRlNzgtODVkMi1mMGZkYzA3YmRhOGMiLCJlbWFpbCI6ImFwcHNAZ2FpYW5zb2x1dGlvbnMuY29tIn0.ZyBbjNdwTWwr0-uYvLpkRIIxLJ8z0njEuK6EkY4xJU5N0_5Dwq_PnhQIJCYz8u4sT7qnXX8l5C0JZy4BIqe0hiuK_7fRN1LDSaAhABbGxYxcn4KbW8WBD29YCk5prM1sEPjO8XD4BffwniaiJJXPJ2eK40X3gRiBv0oy9NS_pQaWSoEIaIUZ2C-W50U-fLli5g2hlPx4l_1APUJ0RE2LjmJQ2M6AmxHGb758YmKLM3X8meVbdrsdqfdXrjN2NTB2_nImYzMn_kkaGWY9v-N5dWwaMOO6eyyPv2SfpysavUQpip1dzjTAkd5sfT9UFB4K5U5uRmJ43rPnXYljz3zuhw',
        'origin': 'https://holacracy.aidtaas.com',
        'referer': 'https://holacracy.aidtaas.com/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
    }

    # Create a dictionary to store image names and corresponding CDN URLs
    image_data_dict = {}

    # Iterate through each file in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip non-image files if needed
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            continue

        # Upload the image and get the CDN URL
        cdn_url = upload_image(file_path, filename, headers, boundary)

        # Store the image name and CDN URL in the dictionary
        image_data_dict[filename] = cdn_url

    # Write the dictionary to a JSON file
    json_file_path = 'logoCDN.json'
    with open(json_file_path, 'w') as json_file:
        json.dump(image_data_dict, json_file, indent=2)

    print(f"CDN URLs written to {json_file_path}")

if __name__ == "__main__":
    main()

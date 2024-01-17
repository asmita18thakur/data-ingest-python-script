import os
import requests
import json

API_URL = "https://ig.aidtaas.com/content-service/v1.0/content/upload/618b6fdef5dacc0001a6b1b0/618b6fdef5dacc0001a6b1b0/618b6fdef5dacc0001a6b1b0"
HEADERS = {"accept": "application/json"}
TAGS = ""
FILE_PATH_ACCESS = "public"
OVERRIDE_FILE = "true"

FOLDER_PATH = "Tenants"

RESPONSES_FILE = f"responses{FOLDER_PATH}.json"

responses = []

for filename in os.listdir(FOLDER_PATH):
    filepath = os.path.join(FOLDER_PATH, filename)
    if os.path.isfile(filepath):
        print(f"Uploading file: {filename}")
        
        files = {"file": (filename, open(filepath, "rb"), "application/octet-stream")}
        params = {
            "filePath": "logs",
            "tags": TAGS,
            "filePathAccess": FILE_PATH_ACCESS,
            "overrideFile": OVERRIDE_FILE,
        }
        
        response = requests.post(API_URL, headers=HEADERS, files=files, params=params)
        
        response_data = {
            "filename": filename,
            "status_code": response.status_code,
            "response_text": response.json().get("cdnUrl")       
        }
        responses.append(response_data)
        
        if response.status_code == 200:
            print(f"Uploaded {filename}")
        else:
            print(f"Failed to upload {filename}. Status code: {response.status_code}")

# Save responses to JSON file
with open(RESPONSES_FILE, "w") as json_file:
    json.dump(responses, json_file, indent=2)

print(f"Responses saved to {RESPONSES_FILE}")



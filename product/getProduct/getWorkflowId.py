import requests
import json

def get_wf_ids(size=200, max_pages=10):
    url = "https://ig.gov-cloud.ai/bob-service/v1.0/wf/home"
    headers = {
        "Authorization": f"Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJhYktCMjBIbEhpclVudTJub1JHclRGSlJibXVqNGIzVlFXa1YwbThTYzZjIn0.eyJleHAiOjE3MTM1MzYyNzUsImlhdCI6MTcxMzUwMDI3NSwianRpIjoiMjVkNWY3MDAtN2ZkYy00ZTRlLWI5ODItMGZiZTBiY2IwMjk3IiwiaXNzIjoiaHR0cDovL2tleWNsb2FrLmtleWNsb2FrLnN2Yy5jbHVzdGVyLmxvY2FsOjgwODAvcmVhbG1zL21hc3RlciIsImF1ZCI6WyJQQVNDQUxfSU5URUxMSUdFTkNFIiwiTU9ORVQiLCJIT0xBQ1JBQ1kiLCJhY2NvdW50IiwiVklOQ0kiXSwic3ViIjoiOTk0ZjgzYzctMWY1ZS00MjhlLTllYzAtYjEwNjMxODUwNGEyIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiQk9MVFpNQU5OX0JPVCIsInNlc3Npb25fc3RhdGUiOiIyNzU1M2YxYS1kYTQwLTQwMmMtOWZiZS04MzM5YTI4ZjI1YjgiLCJuYW1lIjoiVGVuYW50IFRlbmFudCIsImdpdmVuX25hbWUiOiJUZW5hbnQiLCJmYW1pbHlfbmFtZSI6IlRlbmFudCIsInByZWZlcnJlZF91c2VybmFtZSI6InRlbmFudCIsImVtYWlsIjoiYWlkdGFhc0BnYWlhbnNvbHV0aW9ucy5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYWNyIjoiMSIsInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJkZWZhdWx0LXJvbGVzLW1hc3RlciIsIm9mZmxpbmVfYWNjZXNzIiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJCT0xUWk1BTk5fQk9UIjp7InJvbGVzIjpbIkJPTFRaTUFOTl9CT1RfVVNFUiJdfSwiUEFTQ0FMX0lOVEVMTElHRU5DRSI6eyJyb2xlcyI6WyJQQVNDQUxfSU5URUxMSUdFTkNFX1VTRVIiXX0sIk1PTkVUIjp7InJvbGVzIjpbIk1PTkVUX1VTRVIiXX0sIkhPTEFDUkFDWSI6eyJyb2xlcyI6WyJIT0xBQ1JBQ1lfVVNFUiJdfSwiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19LCJWSU5DSSI6eyJyb2xlcyI6WyJWSU5DSV9VU0VSIl19fSwic2NvcGUiOiJlbWFpbCBwcm9maWxlIiwic2lkIjoiMjc1NTNmMWEtZGE0MC00MDJjLTlmYmUtODMzOWEyOGYyNWI4IiwidGVuYW50SWQiOiI5OTRmODNjNy0xZjVlLTQyOGUtOWVjMC1iMTA2MzE4NTA0YTIifQ==.jDtcwSRyrquZDIEjR_f52eafMGE5P9fSedbw6wKtTDRbfEpn7b0ME8-jMS29p8kQCOjVkJUyoMFNxbpu2-XRvKUl2knFWe6fxnr2eJElGyJx-op_jtBXavhl-cNJm4lS1lpoxZs2HmTdSQMg5hYAiO4x8j9ogUol6VWagmADLGzY_Y3mBGLkh5grAYvIi8hPL9rmAQuk_t5JEBTCobhvU-q6XWoxNSxB35AhgHYfMutdauowzQEmoVy0-l3UiAoLG4-A95QD7Cw31ynuNRCEdrB_2NBTxm8pkBJEFJdrAH9y_Cd2bdTDj_70P5Y29nAe_qpxD__oqBMiMbDGxxK_LA",
        "Content-Type": "application/json"
    }
    
    params = {
        "size": size,
        "page":1
    }
    
    wf_ids = []
    while max_pages>0:
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code != 200:
            print(f"Failed to fetch data. Status code: {response.status_code}, Response: {response.text}")
            break
        
        data = response.json()
        if not isinstance(data, list):
            print("Unexpected data format.")
            break
        
        if not data:
            break
        
        # Collect wfIds
        wf_ids.extend([item["wfId"] for item in data if "wfId" in item])

        max_pages -=1

    return wf_ids

def save_wf_ids_to_json(wf_ids, filename="wfIds.json"):
    with open(filename, 'w') as f:
        json.dump(wf_ids, f, indent=4)

def main():
    wf_ids = get_wf_ids(10,10)
    if wf_ids:
        save_wf_ids_to_json(wf_ids)
        print(f"wfIds have been saved to {len(wf_ids)} items in 'wfIds.json'")
    else:
        print("No wfIds were found or saved.")

if __name__ == "__main__":
    main()

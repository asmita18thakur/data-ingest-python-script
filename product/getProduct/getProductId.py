import requests
import openpyxl

def get_product_data(platform_id, size=150):
    url = f"https://ig.gov-cloud.ai/hcy-web/v1.0/product/platform/filter?platformId=66f2dec4b1dbc9702f4049b7&productOffering=PRODUCT&size=50&page=0"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI3Ny1NUVdFRTNHZE5adGlsWU5IYmpsa2dVSkpaWUJWVmN1UmFZdHl5ejFjIn0.eyJleHAiOjE3MjYyMDY2MTQsImlhdCI6MTcyNjE3MDYxNCwianRpIjoiNmY3NDc0YmUtMDcxNS00ZmE3LWI5ZWMtOWM1NGY5YTViN2FhIiwiaXNzIjoiaHR0cDovL2tleWNsb2FrLmtleWNsb2FrLnN2Yy5jbHVzdGVyLmxvY2FsOjgwODAvcmVhbG1zL21hc3RlciIsImF1ZCI6WyJCT0xUWk1BTk5fQk9UIiwiUEFTQ0FMX0lOVEVMTElHRU5DRSIsIlhQWC1DTVMiLCJhY2NvdW50Il0sInN1YiI6IjdjMmEwY2M1LTY5ODgtNDk5OS04ZjZkLTQ4MjM2MzQ4MmVlZiIsInR5cCI6IkJlYXJlciIsImF6cCI6IkhPTEFDUkFDWSIsInNlc3Npb25fc3RhdGUiOiI5ZTBhYjZlNS0yNmI5LTRkOWItODA4ZC0wY2Q0MWU3ZWMyMDUiLCJuYW1lIjoibW9iaXVzIG1vYml1cyIsImdpdmVuX25hbWUiOiJtb2JpdXMiLCJmYW1pbHlfbmFtZSI6Im1vYml1cyIsInByZWZlcnJlZF91c2VybmFtZSI6InBhc3N3b3JkX3RlbmFudF9tb2JpdXNAbW9iaXVzZHRhYXMuYWkiLCJlbWFpbCI6InBhc3N3b3JkX3RlbmFudF9tb2JpdXNAbW9iaXVzZHRhYXMuYWkiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYWNyIjoiMSIsImFsbG93ZWQtb3JpZ2lucyI6WyIvKiJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsiZGVmYXVsdC1yb2xlcy1tYXN0ZXIiLCJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiQk9MVFpNQU5OX0JPVCI6eyJyb2xlcyI6WyJCT0xUWk1BTk5fQk9UX1VTRVIiXX0sIlBBU0NBTF9JTlRFTExJR0VOQ0UiOnsicm9sZXMiOlsiU1VQRVJBRE1JTiJdfSwiWFBYLUNNUyI6eyJyb2xlcyI6WyJYUFgtQ01TX1VTRVIiXX0sIkhPTEFDUkFDWSI6eyJyb2xlcyI6WyJIT0xBQ1JBQ1lfVVNFUiJdfSwiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJwcm9maWxlIGVtYWlsIiwic2lkIjoiOWUwYWI2ZTUtMjZiOS00ZDliLTgwOGQtMGNkNDFlN2VjMjA1IiwidGVuYW50SWQiOiI3YzJhMGNjNS02OTg4LTQ5OTktOGY2ZC00ODIzNjM0ODJlZWYiLCJyZXF1ZXN0ZXJUeXBlIjoiVEVOQU5UIn0=.R4L6stW_Iv-yxf3FeTG5wwoCRD6YpialiDxo1Z1JCsQ168mkhuuFnNRHvyTxHb7DTZBSqjP6wlMsauOR-g9cyuVPx1lKNo4q4cp54AE8gLX09Vw0PqOh103XNaP6-iEClgDPzJgobIE7xGp2Gg7b2ZqqcLe1smiUzy9mUCTyAJRE-7O8FpXLdyJy-jfWGz8eed2-s1ffHIaOXKbWRUjR58mvxTG0ZAwM-1mNuW4eGRJS0QTMYPsYT9bO8PzYdlubl1cFCKmz47x-rlTlyepXesLgw9BYIJCMMCMT1N9T7yejdi_pTBWYismNFRWx6gGYX7cxasAKRernr-RZnHvWMg",
        "Content-Type": "application/json"
    }
    
    params = {
        "size": size,
        "page": 0
    }
    
    products_list = []
    while True:
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code != 200:
            print(f"Failed to fetch data. Status code: {response.status_code}, Response: {response.text}")
            break
        
        data = response.json()
        if "content" not in data:
            print("No product data found.")
            break
        
        products = data["content"]
        if not products:
            break
        
        # Collect product ID and name
        products_list.extend([(product["id"], product["name"]) for product in products])

        # Check if we need to fetch more pages
        params["page"] += 1
        if params["page"] >= data["totalPages"]:
            break

    return products_list

def save_products_to_excel(products, filename="response.xlsx"):
    # Create a new Excel workbook
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    
    # Set the headers for the sheet
    sheet["A1"] = "Product ID"
    sheet["B1"] = "Product Name"
    
    # Populate the Excel sheet with product data
    for row_num, (product_id, product_name) in enumerate(products, start=2):
        sheet[f"A{row_num}"] = product_id
        sheet[f"B{row_num}"] = product_name
    
    # Save the Excel file
    workbook.save(filename)
    print(f"Product data has been saved to '{filename}'")

def main():
    platform_id = "66f2dec4b1dbc9702f4049b7"
    
    products = get_product_data( platform_id)
    if products:
        save_products_to_excel(products)
    else:
        print("No product data was found or saved.")

if __name__ == "__main__":
    main()

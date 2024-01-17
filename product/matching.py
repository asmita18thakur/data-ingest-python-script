import pandas as pd
import json

# Load JSON data from the provided file
json_filename = 'inpt.json'
with open(json_filename, 'r') as json_file:
    json_data = json.load(json_file)

# Load Excel sheet
excel_filename = 'productCreation.xlsx'
sheet_name = 'Sheet1'  # Change this to the actual sheet name
df = pd.read_excel(excel_filename, sheet_name=sheet_name)

# Assuming 'products' is the column name in the Excel sheet
products_column = 'name'

cdn_urls = []  # Array to store CDN URLs

# Iterate through each product in the Excel sheet
for product in df[products_column]:
    print(product)
    cdn_url_found = False
    
    # Look for a matching filename in the JSON data
    for item in json_data:
        if str(product) in str(item['filename']):
            # print("hi")
            cdn_urls.append(item['response_text'])
            cdn_url_found = True
            break
    
    if not cdn_url_found:
        cdn_urls.append("Zero")

# Add 'AccountID' column to DataFrame
df['cdnurl'] = cdn_urls

# Write updated DataFrame back to the same Excel file
df.to_excel('productCreation.xlsx', index=False)

print("done")

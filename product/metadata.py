import pandas as pd
import json

# Load Excel data
df = pd.read_excel('temp.xlsx')
df.fillna("", inplace=True)

# Convert to JSON
json_data = {}

# Grouping by a common identifier (e.g., 'name') assuming it's the column to group by
grouped_data = df.groupby('name')

for group_name, group_data in grouped_data:
    nested_objects = []
    
    for index, row in group_data.iterrows():
        nested_object = {
            "imageUrl": row['imageUrl'],
            "Title": row['Title'],
            "Description": row['Description']
            # Add more fields as needed
        }
        nested_objects.append(nested_object)

    # Assign list of objects to the group_name
    json_data[group_name] = nested_objects

# Write JSON data to a file
output_filename = 'product.json'
with open(output_filename, 'w') as json_file:
    json.dump(json_data, json_file, indent=4)

print(f"JSON data has been written to '{output_filename}'")

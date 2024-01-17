import pandas as pd

def excel_to_json(excel_file_path, json_file_path):
    # Read Excel file into a pandas DataFrame
    df = pd.read_excel(excel_file_path)

    # Convert DataFrame to JSON and save it to a file
    df.to_json(json_file_path, orient='records', lines=True)

# Example usage
excel_file_path = 'temp (1).xlsx'
json_file_path = 'product.json'

excel_to_json(excel_file_path, json_file_path)

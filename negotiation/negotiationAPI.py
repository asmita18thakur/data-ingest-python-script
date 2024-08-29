import pandas as pd
import numpy as np
import hashlib
import pytz
import json
from datetime import datetime

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# Use the absolute path to read the Excel file
df_products = pd.read_excel('tenant.xlsx')

# Initialize lists to store separate DataFrames
sellers = []
buyers = []

# Iterate through the DataFrame in pairs
for i in range(0, len(df_products) - 1, 2):
    tenant_a = df_products.iloc[i]
    tenant_b = df_products.iloc[i + 1]
    
    # Create DataFrames for seller and buyer
    seller_df = pd.DataFrame([tenant_a], columns=df_products.columns)
    buyer_df = pd.DataFrame([tenant_b], columns=df_products.columns)
    
    # Rename columns
    seller_df = seller_df.rename(columns={'TenantID': 'seller_id'})
    buyer_df = buyer_df.rename(columns={'TenantID': 'buyer_id', 'productId': 'app_id'})
    
    # Set 'negotiatedBy' and 'planType'
    seller_df['negotiatedBy'] = 'SELLER'
    buyer_df['negotiatedBy'] = 'BUYER'
    
    seller_df['negotiationRateCardId'] = seller_df['RateCardID']
    
    # Define the sequence of values
    plan_types = ['PLATINUM', 'GOLD', 'SILVER']
    
    # Create a repeated sequence to match the length of the DataFrame
    num_rows = len(seller_df)
    repeated_plan_types = np.tile(plan_types, num_rows // len(plan_types) + 1)[:num_rows]
    
    # Assign the sequence to the 'planType' column
    seller_df['planType'] = repeated_plan_types

    # Append to lists
    sellers.append(seller_df)
    buyers.append(buyer_df)

# Combine all seller and buyer DataFrames into single DataFrames
df_sellers = pd.concat(sellers, ignore_index=True)
df_buyers = pd.concat(buyers, ignore_index=True)

df_sellers = df_sellers[['seller_id', 'productId', 'RateCardID', 'negotiationRateCardId', 'planType', 'parentTenantId', 'negotiatedBy']]
df_buyers = df_buyers[['buyer_id', 'app_id', 'platformID', 'parentTenantId']]


# Perform the merge
df_merge = df_sellers.merge(df_buyers, on='parentTenantId', how='inner')

# Create a unique ID based on concatenated values (or another method)
df_merge['negotiation_id'] = df_merge.apply(lambda row: hashlib.md5(f"{row['parentTenantId']}_{row['seller_id']}_{row['buyer_id']}".encode()).hexdigest(), axis=1)


# Save both DataFrames to an Excel file with separate sheets
with pd.ExcelWriter('Negotiation_response.xlsx') as writer:
    df_merge.to_excel(writer, sheet_name='Negiotiation', index=False)
print("Script completed. Negotiation IDs have been written to the Excel file.")

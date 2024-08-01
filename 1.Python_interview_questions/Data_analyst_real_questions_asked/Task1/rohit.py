import pandas as pd

# Load the data from Excel files
data1 = pd.read_excel('data.xlsx', sheet_name='data1')
data2 = pd.read_excel('data.xlsx', sheet_name='data2')

# Concatenate the 'orderid' and 'Product id' columns to create the primary key
data1['Primary Key'] = data1['orderid'].astype(str) + data1['Product id'].astype(str)
data2['Primary Key'] = data2['orderid'].astype(str) + data2['Product id'].astype(str)

# Identify records present in data1 but missing in data2
missing_records = data1[~data1['Primary Key'].isin(data2['Primary Key'])]

# Display the missing records
print(missing_records)
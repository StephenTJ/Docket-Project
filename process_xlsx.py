import pandas as pd

file_errors_location = 'purchase_detials.xlsx'
# Convert the csv into data frame
df2 = pd.read_excel(file_errors_location)
# Make the group the data according to Supplier name and make a sublist of Po number and Description
grouped_data = df2.groupby('Supplier').agg(
    {'PO Number': list, 'Description': list}).reset_index()
# Convert grouped data into List of Dict and access the suppliers and cascading values of Po number na Description

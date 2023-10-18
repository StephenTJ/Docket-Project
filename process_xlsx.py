import pandas as pd

file_errors_location = 'purchase_detials.xlsx'
df2 = pd.read_excel(file_errors_location)

grouped_data = df2.groupby('Supplier').agg(
    {'PO Number': list, 'Description': list}).reset_index()

print(grouped_data.to_json(orient="records"))

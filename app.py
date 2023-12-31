from flask import Flask, render_template, request
import pandas as pd
import json
import process_xlsx as px

app = Flask(__name__)

# Create a data frame to store the table
data = {
    'Name': [],
    'StartTime': [],
    'EndTime': [],
    'Hours': [],
    'Rate': [],
    'Supplier': [],
    'PurchaseOrder': [],
}

df = pd.DataFrame(data)

# End point to accept the data and display data


@app.route("/", methods=['GET', 'POST'])
def root():
    global df
    if request.method == 'POST':
        inputName = request.form.get('inputName')
        inputStartTime = request.form.get('inputStartTime')
        inputEndTime = request.form.get('inputEndTime')
        inputHours = request.form.get('inputHours')
        inputRate = request.form.get('inputRate')
        inputSupplier = request.form.get('inputSupplier')
        inputPurchaseOrder = request.form.get('inputPurchaseOrder')

        new_data = {
            "Name": inputName,
            "StartTime": inputStartTime+":00",
            "EndTime": inputEndTime+":00",
            "Hours": inputHours,
            "Rate": inputRate,
            "Supplier": inputSupplier,
            "PurchaseOrder": inputPurchaseOrder
        }
        df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)

    df['Index'] = range(1, len(df) + 1)
    data_list = df.to_json(orient="records")
    data_list = json.loads(data_list)
    supplier_list = json.loads(px.grouped_data.to_json(orient="records"))
    return render_template('index.html', data=data_list, supplier_list=supplier_list)


if __name__ == '__main__':
    app.run()

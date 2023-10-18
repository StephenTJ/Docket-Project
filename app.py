from flask import Flask, render_template, request
import pandas as pd
import json
import process_xlsx as px

app = Flask(__name__)

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
print(df)


@app.route("/", methods=['GET', 'POST'])
def root():
    global df  # Declare df as a global variable to modify it
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

        print(inputName, inputStartTime, inputEndTime, inputHours,
              inputRate, inputSupplier, inputPurchaseOrder)

    df['Index'] = range(1, len(df) + 1)
    data_list = df.to_json(orient="records")
    data_list = json.loads(data_list)
    supplier_list = json.loads(px.grouped_data.to_json(orient="records"))

    supplier_list_str = px.grouped_data.to_json(orient="records")
    print(supplier_list_str)
    return render_template('index.html', data=data_list, supplier_list=supplier_list, supplier_list_str=supplier_list_str)


if __name__ == '__main__':
    app.run()

from flask import Flask, render_template, request
import pandas as pd
import json

app = Flask(__name__)

data = {
    'Name': ['John', 'Alice', 'Bob'],
    'StartTime': ['09:00:00', '08:30:00', '10:15:00'],
    'EndTime': ['17:00:00', '16:45:00', '18:30:00'],
    'Hours': [8, 8.5, 8.25],
    'Rate': [10.0, 15.0, 20.0],
    'Supplier': ['Supplier A', 'Supplier B', 'Supplier C'],
    'PurchaseOrder': ['PO-001', 'PO-002', 'PO-003'],
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
    print(type(data_list))
    data_list = json.loads(data_list)
    print(data_list)

    return render_template('index.html', data=data_list)


if __name__ == '__main__':
    app.run()

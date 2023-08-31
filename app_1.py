from flask import Flask, render_template, url_for,request
import pickle
from sklearn.preprocessing import LabelEncoder


model = pickle.load(open("modelkn.pkl",'rb'))
scaler=pickle.load(open('Scaler.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def welcome():
     return render_template("index.html")

@app.route('/predict',methods =['POST'])
def predict():
    NumberofCows=int(request.form['Number of Cows'])
    Total =float(request.form['Total'])
    TotalValue= float(request.form['Total Value'])
    QuantitySold= int(request.form['Quantity Sold (liters/kg)'])
    PriceperUnit_sold = float(request.form['Price per Unit (sold)'])
    QuantityinStock= int(request.form['Quantity in Stock (liters/kg)'])
    MinimumStockThreshold= float(request.form['Minimum Stock Threshold (liters/kg)'])
    PriceperUnit=float(request.form['Price per Unit'])
    #print(Approx. Total Revenue(INR))
    total = [[Total,NumberofCows,PriceperUnit,TotalValue,QuantitySold,PriceperUnit_sold,QuantityinStock,MinimumStockThreshold]]
    print(total) 
    prediction = model.predict(scaler.transform(total))
    print(prediction)
    return render_template ("index.html", ApproxTotalRevenue=prediction)
    
if __name__ == '__main__':
    app.run(debug=False)
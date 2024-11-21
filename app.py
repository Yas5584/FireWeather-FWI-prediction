from flask import Flask,request,render_template,jsonify
import pandas as pd
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
app=Flask(__name__)
Ridge_model=pickle.load(open(r'C:\Users\ys136\Desktop\Data Science\End to End ML Projects\Fire Weather\models\ridge.pkl','rb'))

Standard_scaler=pickle.load(open(r'C:\Users\ys136\Desktop\Data Science\End to End ML Projects\Fire Weather\models\scaler.pkl','rb'))
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict_datapoint',methods=['GET','POST'])
def predict_datapoint():
    if request.method == 'POST':
        Temperature=float(request.form.get('Temperature'))
        RH=float(request.form.get('RH'))
        Ws=float(request.form.get('Ws'))
        Rain=float(request.form.get('Rain'))
        FFMC=float(request.form.get('FFMC'))
        DMC=float(request.form.get('DMC'))
        ISI=float(request.form.get('ISI'))
        Classes=float(request.form.get('Classes'))
        Region=float(request.form.get('Region'))
        newdata_scaled=Standard_scaler.transform([[ Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
        result=Ridge_model.predict(newdata_scaled)

        return render_template("home.html",result=result[0])

    else:
         return render_template("home.html")

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5500,debug=True)



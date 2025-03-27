import numpy as np
import pandas as pd
from flask import Flask , request,jsonify, render_template

import pickle
app=Flask(__name__)

mod=pickle.load(open("model.pkl","rb"))


@app.route("/")
def home():
    return render_template("index.html")



@app.route("/index.html#prediction",methods=['POST'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    a=int_features
    age=int(a[0])
    sex=int(a[1])
    cp=int(a[2])    
    trestbps=int(a[3])
    chol=int(a[4])
    fbs=int(a[5])
    restecg=int(a[6])
    thalach=int(a[7])
    exang=int(a[8])
    oldpeak=int(a[9])
    slope=int(a[10])
    ca=int(a[11])
    thal=int(a[12])
    df=[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
    print(df)
    df=np.array(df).reshape(1,-1)
    prediction=mod.predict(df)
    prediction=int(prediction)
    print(prediction)
    if(prediction==1):
        return render_template("index.html",pred="REPORT:==== Oops , You have the chances of heart Disease")
    else:
        return render_template("index.html",pred="REPORT:==== CONGRATS, You don't have heart disease")
    




if __name__ == "__main__":
    app.run(debug=True)
import numpy as np 
import pandas as pd
from sklearn import metrics
from flask import Flask, request, render_template
import re
import math
import pickle

app = Flask("__name__",template_folder='../templates')
q = ""

@app.route("/")
def loadPage():
	return render_template('templates/home.html', query="")



@app.route("/predict", methods=['POST'])
def DiabetesPrediction():
    df = pd.read_csv('pima-indians-diabetes-2.data')

    df.info()
    print(request.form)

    inputQuery1 = request.form['query1']
    inputQuery2 = request.form['query2']
    inputQuery3 = request.form['query3']
    inputQuery4 = request.form['query4']
    inputQuery5 = request.form['query5']
    inputQuery6 = request.form['query6']
    inputQuery7 = request.form['query7']
    inputQuery8 = request.form['query8']
    
    model=pickle.load(open('model1.sav','rb'))
    
    data = np.array([inputQuery1, inputQuery2, inputQuery3, inputQuery4, inputQuery5,inputQuery6,inputQuery7,inputQuery8]).reshape(1,-1).astype('float64')
    
   # new_df = pd.DataFrame(data, columns = ['Preg', 'Plas', 'Pres', 'Skin', 'Test','mass','Pedi','age'])
    #print(new_df)
    single = model.predict(data)
    #probability = model.predict_proba(new_df)[:,0:8]
    #probability=model.score(data[:][0:8],data[:][8])
    #print(probability)
    print(single)
    if single==1:
        output = "The patient is diagnosed with Diabetes"
        #output1 = "Confidence: {}".format(probability*100)
    else:
        output = "The patient is not diagnosed with Diabetes"
        #output1 = ""
    
    return render_template('home.html', output1=output, query1 = request.form['query1'], query2 = request.form['query2'],query3 = request.form['query3'],query4 = request.form['query4'],query5 = request.form['query5'],query6 = request.form['query6'],query7 = request.form['query7'],query8 = request.form['query8'])
    
if __name__ == "__main__":
    app.run(debug=True)

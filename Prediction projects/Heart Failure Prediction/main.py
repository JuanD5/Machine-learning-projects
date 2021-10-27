import pickle
import numpy as np
from flask import Flask, request, render_template

filename = 'randomForest.pkl'
model = pickle.load(open(filename,'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
    

# Model prediction. 
@app.route('/predict',methods = ['POST'])
def predict():
    
    if request.method == 'POST':
        
        e_f = int(request.form['ejection_fraction'])
        s_c = float(request.form['serum_creatinine'])
        age = float(request.form['age'])
        c_f = int(request.form['creatinine_phosphokinase'])
        pl = float(request.form['platelets'])
        s_s = int(request.form['serum_sodium'])
        sex = int(request.form['sex'])
       
        data = np.array([e_f,s_c,age,c_f,pl,s_s,sex])
        
        model_prediction = model.predict(data)
        
        model_probability = np.max(model.predict_proba(data))
        
    return render_template('results.html', prediction = model_prediction, probability = model_probability)


if __name__ == '__main__':
    app.run(debug=True)
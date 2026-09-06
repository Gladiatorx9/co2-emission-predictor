#lets import the libraries
import numpy as np
from flask import Flask,render_template,request
import pickle

#lets initalize the flask app
app= Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

#lets define the routr for thr default page 
@app.route('/')
def home():
    return render_template('index.html')

#lets redirect the ApI to predict the c02 emissions
#to use perdict button in our web page 
@app.route('/predict',methods=['post'])
def predict():
    #for rendering results on HTML GUI
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0],2)
    return render_template('index.html',prediction_text='C02 Emission of the vehicle is:{}'.format(output))
   

#staritng the flask server 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
import pandas as pd
from sklearn.linear_model import LinearRegression

import pickle 

df = pd.read_csv("FuelConsumption.csv")

#lets use required features 


cdf = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS']]

#LETS TRAIN THE data and predictor variables

x = cdf.iloc[:,:3]
y = cdf.iloc[:,-1]

regressor =LinearRegression()
#lets train the model 
#training the model with training data
regressor.fit(x,y)

#saving the model to the current directory 
#pickle serializers objects so they can be saved to a file ,and loaded in a
#program again lterr on.

pickle.dump(regressor,open('model.pkl','wb'))

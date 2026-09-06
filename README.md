# CO₂ Emission Predictor

I built this project to understand how a machine learning model can be turned into a working web application.

The application takes a few basic details about a vehicle — **engine size, cylinders, and fuel consumption** — and predicts its CO₂ emissions.

I used **Python and Scikit-learn** to train the model, **Flask** to build the web application, and **Docker** to package everything so the application can run in a consistent environment.

## What does it do?

You can select a vehicle from the interface and enter its specifications. The application then sends the values to the trained machine learning model and displays the predicted CO₂ emissions.

I also added different vehicle background videos to make the interface more interactive.

Currently, the available vehicles are:

* BMW
* Lamborghini
* McLaren
* Porsche 911

The vehicle information can also be changed manually, so you can experiment with different values and see how they affect the prediction.

## How the ML model works

The model is a **Linear Regression** model.

It was trained using vehicle fuel-consumption data from `FuelConsumption.csv`.

### Inputs

* Engine Size
* Cylinders
* Combined Fuel Consumption


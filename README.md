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

### Output

* Predicted CO₂ Emissions

After training, the model is saved as:

```text
model.pkl
```

The Flask application loads this model and uses it whenever a prediction is requested.

## Project Flow

```text
User
 ↓
Web Interface
 ↓
Vehicle Information
 ↓
Flask Application
 ↓
ML Model
 ↓
CO₂ Prediction
 ↓
Result displayed on screen
```

## Technologies I used

* Python
* Pandas
* NumPy
* Scikit-learn
* Flask
* HTML
* CSS
* JavaScript
* Docker
* Git & GitHub
* Git LFS

## Project Structure

```text
co2-emission-predictor/
│
├── app.py
├── mml.py
├── model.pkl
├── FuelConsumption.csv
├── requirements.txt
├── Dockerfile
├── README.md
├── .gitignore
├── .gitattributes
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── video/
│       ├── Bmw.mp4
│       ├── Lamborghini.mp4
│       ├── McLaren.mp4
│       └── Porsche911.mp4
│
└── templates/
    └── index.html
```

## Running the project locally

First install the required Python packages:

```bash
pip install -r requirements.txt
```

Then start the Flask application:

```bash
python app.py
```

Open the application in your browser:

```text
http://localhost:5000
```

## Running with Docker

I also containerized the application using Docker.

Build the image:

```bash
docker build -t co2-emission-predictor .
```

Run the container:

```bash
docker run -d -p 5000:5000 --name co2-app co2-emission-predictor
```

Then open:

```text
http://localhost:5000
```

To check the running container:

```bash
docker ps
```

To view the application logs:

```bash
docker logs co2-app
```

To stop the application:

```bash
docker stop co2-app
```

## Why I made this project

I wanted to work on something that combines **Machine Learning with practical application and DevOps concepts**, rather than only training a model inside a notebook.

Through this project I worked with:

* Preparing data for a machine learning model
* Training and saving a model
* Connecting the model with Flask
* Building a simple interactive frontend
* Creating a Docker image
* Running the application inside a container
* Managing the project with Git and GitHub
* Using Git LFS for large video files

## What's next?

There are a few things I would like to add as I continue improving the project:

* Add automated testing
* Create a GitHub Actions CI/CD pipeline
* Publish the Docker image
* Add application monitoring
* Improve the ML model and compare it with other algorithms
* Deploy the application to the cloud

---

**Built as a hands-on project to learn and practice Machine Learning, Python, Flask, Docker, and DevOps.**

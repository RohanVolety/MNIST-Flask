# MNIST Image classification

This is a Deep Learning project featuring the MNIST dataset. I have used a simple CNN model to classify the dataset with accuracy of 98.56%.The Model is then deployed on the webpage using Flask.

## Prerequisites 

Ensure that you have Docker, Minikube, and kubectl installed before running these commands

## Create Virtual Environment
Open a terminal and navigate to your project folder.
Use the following command to create a virtual environment named venv:
```
python3 -m venv venv

```
Activate the Virtual Environment:
```
venv\Scripts\activate
```
Install required Libraries

```
pip install -r requirements.txt
```

## How to run the project
```
git clone https://github.com/RohanVolety/MNIST-Flask.git

cd MNIST-FLASK

```


## Basic Configurations
In ```app.py```, update the database configuration:
```

db_config = {
    'host': '127.0.0.1',
    'user': '',
    'password': '',
    'port':3306

}
change the user and password with your SQL user and password. 
```


## Using Python (Locally)

```python
python app.py
```

## Using Docker 
In ```app.py```, update the database configuration:

Build and run the Docker container:

```
docker-compose build

docker-compose up

```

## Using Kubernetes


```
- run minikube
minikube start

- Build our flask image
docker build -t mnist-classifier .

- Test flask image by running on localhost
docker run -p 5000:5000 mnist-classifier

- Deploy flask image
kubectl apply -f deployment.yaml

```


# MNIST Image classification

This is a Deep Learning project featuring the MNIST dataset. I have used a simple CNN model to classify the dataset with accuracy of 98.56%.The Model is then deployed on the webpage using Flask.

## Prerequisites 

Ensure that you have Docker, Minikube, and kubectl installed before running these commands


## How to run the project
```
git clone 

cd MNIST

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

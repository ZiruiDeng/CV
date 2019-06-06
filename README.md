
# Introduction

This project deploys MNIST application into the container. Users submit digital pictures with handwritten characters through curl-XPOST command. This program first recognizes the pictures, and then returns the recognized numbers to users. Every time a user submits an image, identifies a text and timestamp information in MNIST, it is recorded in Cassandra for storage.


The web service is created using Flask, and the prediction model is the Softmax model from Tensorflow tutorial. The prediction model is exported using tensorflow.builder, and loaded when building Docker Container under app.py. Next we have the online database. Online database is achieved using Cassandra through Docker. First we launch as Cassandra image, configure it using cqlsh, then link the container we built earlier with this Cassandra image.


The Cassandra Database records the user IP address, the service request time, the predicted result, and the path to the uploaded image. Finally, the application currently uses a MNIST model trained by 10000 steps and provides the prediction service with an accuracy of 0.92.  


## Cassandra Container Preparation
The administrator can pull the image from Docker Hub by the following command:
```
docker pull Cassandra
```

To construct the Docker Container:
```
docker run --name ll-cassandra -p 9042:9042 -d cassandra:latest
```

## Application Container Preparation
The administrator may build the image from the Dockerfile using the following command:
```
docker build --tag=big-data .
```

To run the Docker Container in detached mode:
```
docker run -d -p 4000:80 big-data
```

## Docker Run
After tagging image to the repository, the administrator may use "docker run" to run the app on any machine:
```
docker run -p 4000:80 kendeng1127/project-bigdata:bigdata
```

## Submit Prediction
Use the following curl command to submit prediction to Application Docker Container.<br/>
```
curl -X POST -F image=@[path_to_the_image] '[url_to_the_service]'
```


## Use Web to Submit Images
The app can be run on localhost:4000. Refer to the project report file for more details.

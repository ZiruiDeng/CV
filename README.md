
*Introduction

This project deploys MNIST application into the container. Users submit digital pictures with handwritten characters. This program first recognizes the pictures, and then returns the recognized numbers to users. Every time a user submits an image, identifies a text and timestamp information in MNIST, it is recorded in Cassandra for storage.


*Files

app.py: main program

model.py: mnist model architecture

predict.py: the program for predicting numbers

dockerfile

requirements.txt



some pictures of numbers used to test the app 

snapshots of the app running

perserved mnist model after training

big-data project report

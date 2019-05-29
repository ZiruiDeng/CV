from model import Network
from predict import Predict
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import tensorflow as tf
import numpy as np
import datetime
import os
from cassandra.cluster import Cluster
from PIL import Image
from tensorflow.python.saved_model import tag_constants
import logging
app = Flask(__name__)
ALLOWED_EXTENSIONS = set([ 'pdf', 'png', 'jpg', 'jpeg'])
KEYSPACE = "demandkeyspace"

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return '''
    <!doctype html>
    <html>
    <body>
    <form action='/predict' method='post' enctype='multipart/form-data'>
        <input type='file' name='file'>
    <input type='submit' value='提交'>
    </form>
    '''  

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        #In case no file was uploaded
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        #In case file has an empty name
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        #Everything is correct and we can run the prediction
        if file and allowed_file(file.filename):
            #save and read uploaded image
            filename = secure_filename(file.filename)
            file.save(secure_filename(file.filename))
            image = Image.open(file.filename)
            #flatten_img = np.reshape(image, 784)
            app = Predict()
            x=app.predict(image)
            current_time = str (datetime.datetime.now())
            session.execute(
            """
            INSERT INTO demandtable (time, filename, result)
            VALUES (%s, %s, %s)
            """,
            (current_time,filename,x)
            )
            return '识别结果：'  + x 




if __name__ == '__main__':
    cluster = Cluster(['ll-cassandra'])
    session = cluster.connect(KEYSPACE)
    app.run(host='0.0.0.0', port=9042)
    #app.run(debug=True)

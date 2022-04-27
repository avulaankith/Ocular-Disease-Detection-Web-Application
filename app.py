import os
from werkzeug.utils import secure_filename
from email.policy import default
from wsgiref.validate import validator
from flask import Flask, flash, render_template, redirect, request, url_for, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import cv2
import numpy as np
from keras.preprocessing import image
from keras.applications.resnet import preprocess_input
import tensorflow as tf
from keras.models import load_model

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png',
                      'jpg', 'jpeg', 'gif', 'zip', 'csv', 'png'}

app = Flask(__name__)
app.config['SECRET_KEY'] = "Your_secret_string"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


class Signup(db.Model):

    # sno, name, email, password, date

    # sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(30), nullable=False, primary_key=True)
    password = db.Column(db.String(20), nullable=False)
    date = db.Column(db.String(12), nullable=True)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.name}"


# class Contact(db.Model):

#     # sno, name, email, message, date

#     sno = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(40), nullable=False)
#     email = db.Column(db.String(30), nullable=False)
#     message = db.Column(db.String(120), nullable=False)
#     date = db.Column(db.String(12), nullable=True)


@app.route("/", methods=['GET', 'POST'])
def home():

    # if(request.method == 'POST'):
    #     name = request.form.get('name')
    #     email = request.form.get('email')
    #     message = request.form.get('message')

    #     entry1 = Contact(name=name, email=email,
    #                      message=message, date=datetime.now())
    #     db.session.add(entry1)
    #     db.session.commit()

    return render_template("index.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if(request.method == 'POST'):
        # Add entry to the data base
        email = request.form['email']
        password = request.form['password']

        todo = Signup.query.filter_by(email=email).first()
        if (email == todo.email) and (password == todo.password):
            return render_template("dashboard.html")

    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if(request.method == 'POST'):
        # Add entry to the data base
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        entry = Signup(name=name, email=email,
                       password=password, date=datetime.now())
        db.session.add(entry)
        db.session.commit()
        return redirect("/")

    return render_template('signup.html')


@app.route('/dashboard')
def dashboad():
    return render_template('dashboard.html')


@app.route('/prediction_form')
def prediction_form():
    return render_template('pred_form.html')


@app.route('/uploads/<name>')
def download_file(name):
    # return send_from_directory(app.config["UPLOAD_FOLDER"], name)
    return render_template("success.html", name=name)


@app.route('/success', methods=['POST', 'GET'])
def success():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_file', name=filename))


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/predict_image/<name>")
def predict_image(name):
    model = load_model('vgg16_1.h5')
    img = image.load_img("uploads/"+name, target_size=(224, 224))
    x = image.img_to_array(img)
    x = x/255
    x = np.expand_dims(x, axis=0)
    img_data = x
    # model.predict(img_data)
    a = np.argmax(model.predict(img_data), axis=1)
    if(a == 0):
        temp = "Cataract"
    else:
        temp = "Normal"
    return render_template("output.html", temp=temp)


if __name__ == "__main__":
    app.run(debug=True)

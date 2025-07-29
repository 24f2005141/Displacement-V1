from flask import Flask,render_template,request,url_for,redirect,flash,session

app=Flask(__name__)

app.config['SECRET_KEY'] = 'your_secret_key1234'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vehicle_parking_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
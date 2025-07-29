from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    phone_no = db.Column(db.String(15), unique=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='user')
    
    # Relationships
    owned_spaces = db.relationship('ParkingSpace', backref='owner', lazy=True, cascade='all, delete-orphan')
    reservations = db.relationship('Reservations', backref='user', lazy=True)


class ParkingSpace(db.Model):
    __tablename__ = 'parking_spaces'
    
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    address = db.Column(db.String(500), nullable=False)
    pin_code = db.Column(db.String(10), nullable=False)
    gmap_link = db.Column(db.String(1000)) 
    security = db.Column(db.Boolean, nullable=False)
    cctv = db.Column(db.Boolean, nullable=False)
    covered = db.Column(db.Boolean, nullable=False)
    length = db.Column(db.Float, nullable=False)
    width = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)
    
    # Relationships
    reservations = db.relationship('Reservations', backref='parking_space', lazy=True)


class Reservations(db.Model):
    __tablename__ = 'reservations'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    parking_space_id = db.Column(db.Integer, db.ForeignKey('parking_spaces.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    transcation_id = db.Column(db.String(50), nullable=False)
    
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Retreat(db.Model):
    __tablename__ = 'retreats'              #Database table
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(50), nullable=False)
    condition = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(200), nullable=False)
    tag = db.Column(db.ARRAY(db.String), nullable=False)
    duration = db.Column(db.Integer, nullable=False)

class Booking(db.Model):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    user_name = db.Column(db.String(100), nullable=False)
    user_email = db.Column(db.String(100), nullable=False)
    user_phone = db.Column(db.String(20), nullable=False)
    retreat_id = db.Column(db.Integer, db.ForeignKey('retreats.id'), nullable=False)
    payment_details = db.Column(db.String(100), nullable=False)
    booking_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    retreat = db.relationship('Retreat')

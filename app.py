from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://postgres:Rashi123@localhost/retreat_db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Retreat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String(50), nullable=False)
    condition = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(200), nullable=False)
    tag = db.Column(db.ARRAY(db.String), nullable=False)
    duration = db.Column(db.Integer, nullable=False)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    user_name = db.Column(db.String(100), nullable=False)
    user_email = db.Column(db.String(100), nullable=False)
    user_phone = db.Column(db.String(20), nullable=False)
    retreat_id = db.Column(db.Integer, db.ForeignKey('retreat.id'), nullable=False)
    retreat = db.relationship('Retreat', backref=db.backref('bookings', lazy=True))
    payment_details = db.Column(db.String(200), nullable=False)
    booking_date = db.Column(db.DateTime, nullable=False)

@app.cli.command("initdb")
def initdb_command():
    """Initialize the database."""
    db.create_all()
    load_mock_data()
    print("Initialized the database.")

def load_mock_data():
    with open('mock_data.json') as f:
        data = json.load(f)
        for item in data:
            retreat = Retreat(
                id=item['id'],
                title=item['title'],
                description=item['description'],
                date=datetime.fromtimestamp(item['date']),
                location=item['location'],
                price=item['price'],
                type=item['type'],
                condition=item['condition'],
                image=item['image'],
                tag=item['tag'],
                duration=item['duration']
            )
            db.session.add(retreat)
        db.session.commit()

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Wellness Retreat Platform API!"

@app.route('/retreats', methods=['GET'])
def get_retreats():
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 5, type=int)
    pagination = Retreat.query.paginate(page, limit, False)
    retreats = pagination.items
    return jsonify([{
        'id': retreat.id,
        'title': retreat.title,
        'description': retreat.description,
        'date': retreat.date.timestamp(),
        'location': retreat.location,
        'price': retreat.price,
        'type': retreat.type,
        'condition': retreat.condition,
        'image': retreat.image,
        'tag': retreat.tag,
        'duration': retreat.duration
    } for retreat in retreats])


@app.route('/book', methods=['POST'])
def create_booking():
    data = request.get_json()
    existing_booking = Booking.query.filter_by(user_id=data['user_id'], retreat_id=data['retreat_id']).first()
    if existing_booking:
        return jsonify({'error': 'User has already booked this retreat'}), 400
    booking = Booking(
        user_id=data['user_id'],
        user_name=data['user_name'],
        user_email=data['user_email'],
        user_phone=data['user_phone'],
        retreat_id=data['retreat_id'],
        payment_details=data['payment_details'],
        booking_date=datetime.strptime(data['booking_date'], '%Y-%m-%d')
    )
    db.session.add(booking)
    db.session.commit()
    return jsonify({'message': 'Booking created successfully'}), 201

@app.route('/retreats/filter', methods=['GET'])
def filter_retreats():
    filter_criteria = request.args.get('filter')
    retreats = Retreat.query.filter(Retreat.title.ilike(f'%{filter_criteria}%')).all()
    return jsonify([{
        'id': retreat.id,
        'title': retreat.title,
        'description': retreat.description,
        'date': retreat.date.timestamp(),
        'location': retreat.location,
        'price': retreat.price,
        'type': retreat.type,
        'condition': retreat.condition,
        'image': retreat.image,
        'tag': retreat.tag,
        'duration': retreat.duration
    } for retreat in retreats])

@app.route('/retreats/search', methods=['GET'])
def search_retreats():
    search_term = request.args.get('search')
    retreats = Retreat.query.filter(Retreat.title.ilike(f'%{search_term}%')).all()
    return jsonify([{
        'id': retreat.id,
        'title': retreat.title,
        'description': retreat.description,
        'date': retreat.date.timestamp(),
        'location': retreat.location,
        'price': retreat.price,
        'type': retreat.type,
        'condition': retreat.condition,
        'image': retreat.image,
        'tag': retreat.tag,
        'duration': retreat.duration
    } for retreat in retreats])

if __name__ == '__main__':
    app.run(debug=True)

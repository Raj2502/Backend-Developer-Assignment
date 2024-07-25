# Backend-Developer-Assignment

Flask Retreat Management System
A Flask-based web application to manage and book retreats. This application allows users to view retreats, search for specific ones, and book them.

Features
View Retreats: List all available retreats with pagination.
Search Retreats: Search retreats by title.
Filter Retreats: Filter retreats based on various criteria.
Book Retreats: Create and manage bookings for retreats.
Installation
Prerequisites
Python 3.x
PostgreSQL (or another supported database)
Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/your-repository.git
cd your-repository
Create and Activate a Virtual Environment
bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Dependencies
bash
Copy code
pip install -r requirements.txt
Configure the Database
Create a PostgreSQL database (or configure another database as needed).

Set the DATABASE_URL environment variable to your database URI. For PostgreSQL, it might look like this:

bash
Copy code
export DATABASE_URL='postgresql://username:password@localhost/yourdatabase'
On Windows, use set instead of export:

bash
Copy code
set DATABASE_URL=postgresql://username:password@localhost/yourdatabase
Run Migrations
bash
Copy code
flask db upgrade
Start the Application
bash
Copy code
flask run
The application will be accessible at http://127.0.0.1:5000.

API Endpoints
GET /retreats
Retrieve a list of all retreats with pagination.

Query Parameters:

page: Page number (default: 1)
limit: Number of retreats per page (default: 5)
GET /retreats/filter
Filter retreats by title.

Query Parameters:

filter: Filter criteria
GET /retreats/search
Search for retreats by title.

Query Parameters:

search: Search term
POST /book
Create a new booking.

Request Body:

json
Copy code
{
  "user_id": "123",
  "user_name": "Raj",
  "user_email": "raj.k@example.com",
  "user_phone": "7709580619",
  "retreat_id": "1",
  "payment_details": "Payment information",
  "booking_date": "2024-07-25"
}
Contributing
If you'd like to contribute to this project:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature/your-feature).
Create a new Pull Request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Flask for the web framework.
SQLAlchemy for database ORM.
PostgreSQL for the database.

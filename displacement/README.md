🚗 Displacement – Turn Your Driveway Into Income
Displacement is a full-stack web application that transforms private driveways and parking spots into rentable assets. Homeowners (hosts) can list their unused parking spaces, while drivers (renters) can seamlessly search and book them. With support for EV charging, instant booking, and optional car services, Displacement makes urban parking smarter and more sustainable.

🌟 Key Features
🧑‍💼 For Space Owners (Hosts)
📍 List private parking spaces (driveways, garages, etc.)

📆 Set availability windows (by date & time)

💰 Define rates (hourly, daily, or fixed)

🔌 Mark if EV charging is available

🧽 Offer optional services (car wash, interior cleaning)

📊 View bookings, earnings, and space details

📸 Upload and manage space photos

🚙 For Renters (Drivers)
🔍 Search and filter by location, price, availability, EV support

⚡ Book instantly or view slot availability

🧾 Track booking history and invoices

💼 Add optional services during booking

🗺️ Integrated Google Maps for space location

💎 General Highlights
🌗 Responsive mobile-first UI with Dark Mode toggle

🎨 Clean, modern UI with gradients and smooth animations

🔒 Secure Sign In / Sign Up with Flask sessions

🚥 Role-based access: Host / Renter dashboards

📦 Modular codebase for scalability

🛠 Tech Stack
Layer	Technology / Tools	Description
🧠 Backend	Flask (Python)	Lightweight WSGI framework for routing, session management, authentication
🎨 Frontend	HTML5, CSS3, Bootstrap 5	Template-based UI using Jinja2 and responsive Bootstrap styling
🧩 Templates	Jinja2	Server-side templating for dynamic HTML rendering
📂 ORM	SQLAlchemy (Flask-SQLAlchemy)	Object Relational Mapping for managing database models
🗂️ Database	SQLite	Lightweight database for local development
🖼️ File Upload	Flask-Uploads, FileSystem	Used to handle parking space image uploads
🗺️ Map Embed	Google Maps Embed API	Display parking locations visually
🌐 Deployment	Uvicorn / Gunicorn, Docker-ready	Production-ready deployment stack

🚀 Getting Started
🔧 Prerequisites
Make sure you have the following installed:

Python 3.8+

pip (Python package manager)

Git

📥 Installation
bash
Copy
Edit
# Clone the repository
git clone https://github.com/your-username/displacement-app.git
cd displacement-app

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
🧪 Running the App
bash
Copy
Edit
# Start the Flask server
flask run

# Or with custom port
flask run --host=0.0.0.0 --port=5001
Default URL: http://localhost:5000

📂 Folder Structure
csharp
Copy
Edit
displacement-app/
│
├── static/               # CSS, images, uploaded photos
├── templates/            # Jinja2 HTML templates
│   ├── user/             # Renter views
│   └── host/             # Space owner views
│
├── app.py                # Main Flask application
├── models.py             # SQLAlchemy database models
├── forms.py              # WTForms (if used)
├── requirements.txt      # Python dependencies
└── README.md             # You're here!
🛡️ Security & Enhancements
Passwords are securely hashed using werkzeug.security.

User sessions are managed via Flask's session module.

Input validations and CSRF protection (with Flask-WTF) can be added.

Ready for upgrade to PostgreSQL or MySQL.

🧠 Future Plans
Payment integration (Stripe or Razorpay)

Notifications & email receipts

Ratings and reviews for renters & hosts

QR code check-in/out for reserved spaces

Progressive Web App (PWA) mode

📃 License
This project is open-source and available under the MIT License.

Let me know if you want to add:

screenshots

database schema preview

a deploy-to-render or Docker section
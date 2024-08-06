# Simple Gunicorn Python script

# Import the Flask app
from my_flask_app import app

# Run the app using Gunicorn
app.run(host="0.0.0.0", port=8080)


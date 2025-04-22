from flask import Flask
from app.routes import configure_routes  # Import the routes function
import os

# Initialize Flask app
app = Flask(__name__, template_folder=os.path.join("app", "templates"))  # Use os.path.join for cross-platform compatibility

# Configure routes (from app/routes.py)
configure_routes(app)

if __name__ == "__main__":
    # Run the server
    app.run(debug=True)
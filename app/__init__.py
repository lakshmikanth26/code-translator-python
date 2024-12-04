from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()  # Load API key from .env file

def create_app():
    app = Flask(__name__)
    app.config['GEMINI_API_KEY'] = os.getenv('GEMINI_API_KEY')
    
    with app.app_context():
        from . import routes  # Import routes
    return app

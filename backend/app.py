import sys
import os

# Voeg de 'src' map toe aan het pad zodat imports werken
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from flask import Flask
from flask_cors import CORS
from routes.api import api_bp
from models.user import db

# --- SUPABASE CLIENT TOEVOEGEN ---
from supabase import create_client, Client

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_SERVICE_KEY = os.environ.get("SUPABASE_SERVICE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)
# --- EINDE SUPABASE CLIENT TOEVOEGEN ---

app = Flask(__name__)

CORS(app, resources={
    r"/*": {
        "origins": [
            "http://localhost:8080",               # voor lokale testing
            "https://cryptext-x.netlify.app/"   # vervang met jouw echte Netlify URL
        ],
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type"],
        "supports_credentials": True
    }
})

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crypText.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db.init_app(app)

# Register blueprints
app.register_blueprint(api_bp)

# Create database tables
with app.app_context():
    db.create_all()

# (OPTIONEEL) Voorbeeld route die Supabase gebruikt:
@app.route('/api/supabase-users')
def get_supabase_users():
    response = supabase.table('users').select('*').execute()
    return response.data

if __name__ == '__main__':
    app.run(debug=True, port=5000)

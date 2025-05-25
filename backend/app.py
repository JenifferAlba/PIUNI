from flask import Flask
from flask_cors import CORS
from config import Config
from models import db
from routes import api

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
CORS(app)
app.register_blueprint(api)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
 import os
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('postgresql://postgres:ZAAjwdzqFyuNVganVwaotgGivnJngaHy@centerbeam.proxy.rlwy.net:55389/railway')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
   
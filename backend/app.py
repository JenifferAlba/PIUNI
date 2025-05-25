from flask import Flask
from flask_cors import CORS
from config import Config
from models import db
from routes import api
import os

app = Flask(__name__)
app.config.from_object(Config)

# Substitua pela sua string de conexão real, se necessário

db.init_app(app)
CORS(app)
app.register_blueprint(api)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)


   
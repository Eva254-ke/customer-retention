from flask import Flask
from flask_cors import CORS
from routes.events import event_routes

app = Flask(__name__)
CORS(app)

app.register_blueprint(event_routes)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
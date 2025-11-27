from flask import Flask
from flask_cors import CORS
from routes.gateway import gateway_routes

app = Flask(__name__)
CORS(app)

app.register_blueprint(gateway_routes)

@app.route('/')
def index():
    return "Welcome to the Retain API Gateway"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
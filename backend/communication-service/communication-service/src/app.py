from flask import Flask
from routes.communications import communications_blueprint

app = Flask(__name__)

# Register the communications blueprint
app.register_blueprint(communications_blueprint)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
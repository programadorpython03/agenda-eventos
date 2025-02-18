from flask import Flask
from src.main.server.routes.event import event_route_bp

app = Flask(__name__)

app.register_blueprint(event_route_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)


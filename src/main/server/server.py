from flask import Flask
from src.main.routes.event_route import event_route_bp
from src.main.routes.subscriber_route import subscriber_route_bp    
from src.main.routes.events_links_route import events_links_route_bp

app = Flask(__name__)

app.register_blueprint(event_route_bp)
app.register_blueprint(subscriber_route_bp)
app.register_blueprint(events_links_route_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)


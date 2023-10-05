from flask import Flask
from configuration import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    from models import db
    db.init_app(app)
    with app.app_context():
        import routes
        db.create_all()
    return app
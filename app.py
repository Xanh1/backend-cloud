from flask import Flask
from flask_cors import CORS

def create_app():

    app = Flask(__name__, instance_relative_config=False)

    CORS(app)

    with app.app_context():

        from routes.route_user import url_user
        app.register_blueprint(url_user)

    return app
from flask import Flask

def create_app():

    app = Flask(__name__, instance_relative_config=False)

    with app.app_context():

        from routes.route_user import url_user
        app.register_blueprint(url_user)

    return app
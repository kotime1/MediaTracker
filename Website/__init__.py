from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET KEY'] = '5af2568f3ae4e3c92a4c9d5e5f861f2c7bce174c6e688478d3b964e6a3d0bbf2'

    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
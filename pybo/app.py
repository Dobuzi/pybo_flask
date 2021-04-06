from flask import Flask
from views import main_views

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_views.bp)

    return app

if __name__=='__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
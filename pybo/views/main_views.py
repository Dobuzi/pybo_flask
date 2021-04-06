from flask import Blueprint, render_template

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return render_template('index.html')

@bp.route('/')
def index():
    return 'pybo index'
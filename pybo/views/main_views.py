from flask import Blueprint, render_template
import sqlite3

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    db_file = 'database/database.db'
    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute('SELECT id, name FROM user')
    rows = cur.fetchall()
    return render_template('index.html', rows=rows)

@bp.route('/')
def index():
    return 'pybo index'
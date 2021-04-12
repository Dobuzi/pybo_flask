from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\xa5\x13\x1d\x16\x02\x0bV\x00\xe4t\xe3\xa5\x85lz\xa7'

from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'mycar.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\xb1kQO\xeb\xf5\xf7\xb6\xe9\xa0\xf3a\x94\xc6\xd2\xc6'
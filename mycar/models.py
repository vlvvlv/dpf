from mycar import db

class Dpfcar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    carnumber = db.Column(db.String(15), unique=True, nullable=False)
    carnumber4 = db.Column(db.String(4), nullable=False)
    caryear = db.Column(db.String(4), nullable=False)
    carkind = db.Column(db.String(10), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(50), unique=True, nullable=False)
    userpassword = db.Column(db.String(200), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    usertel = db.Column(db.String(50), nullable=False)
    useremail = db.Column(db.String(120), unique=True, nullable=False)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dpfcar_id = db.Column(db.Integer, db.ForeignKey('dpfcar.id', ondelete='CASCADE'))
    dpfcar = db.relationship('Dpfcar', backref=db.backref('contact_set'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    user = db.relationship('User', backref=db.backref('contact_set'))
    ownername = db.Column(db.String(100), nullable=False)
    ownertel = db.Column(db.String(50), nullable=False)
    owneretc = db.Column(db.Text())
    licenseimg = db.Column(db.BLOB)
    create_date = db.Column(db.DateTime(), nullable=False)
    update_date = db.Column(db.DateTime())
    ownernum4 = db.Column(db.String(4))
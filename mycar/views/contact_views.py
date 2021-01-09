from flask import Blueprint, render_template, url_for, request, g, flash
from werkzeug.utils import redirect
from mycar import db
from mycar.models import Dpfcar, Contact
from datetime import datetime
from mycar.views.auth_views import login_required
from sqlalchemy import and_, or_
bp = Blueprint('contact', __name__, url_prefix='/contact')


@bp.route('/regit/<int:dpfcar_id>/')
@login_required
def regit(dpfcar_id):
    dpfcar_one = Dpfcar.query.get_or_404(dpfcar_id)
    return render_template('contact/regit.html', dpfcar_one=dpfcar_one)


@bp.route('/create', methods=('POST',))
@login_required
def create():
    dpfcar_id = request.form['carid']
    ownername = request.form['ownername']
    ownertel = request.form['ownertel']
    owneretc = request.form['owneretc']
    ownernum4 = request.form['ownernum4']

    dpfcar_one = Dpfcar.query.get_or_404(dpfcar_id)
    contact_one = Contact(dpfcar=dpfcar_one, user=g.user, ownername=ownername, ownertel=ownertel,
                          owneretc=owneretc, ownernum4 = ownernum4, create_date=datetime.now(), update_date=datetime.now())

    dpfcar_one.contact_set.append(contact_one)
    g.user.contact_set.append(contact_one)
    db.session.commit()
    return redirect(url_for('contact.result'))


@bp.route('/update', methods=('GET','POST'))
@login_required
def update():
    contact = Contact.query.filter_by(id=request.form['contactid']).first()
    contact.ownername = request.form['ownername']
    contact.ownertel = request.form['ownertel']
    contact.owneretc = request.form['owneretc']
    contact.ownernum4 = request.form['ownernum4']
    contact.update_date = datetime.now()
    db.session.commit()
    return redirect(url_for('contact.result'))


@bp.route('/modify/<int:contact_id>', methods=('GET',))
@login_required
def modify(contact_id):
    contact = Contact.query.get_or_404(contact_id)
    return render_template('contact/update.html', contact_one=contact)


@bp.route('/delete/<int:contact_id>', methods=('GET',))
@login_required
def delete(contact_id):
    contact = Contact.query.get_or_404(contact_id)
    if g.user != contact.user:
        flash('삭제권한이 없습니다')
        return redirect(url_for('contact.result'))
    db.session.delete(contact)
    db.session.commit()
    return redirect(url_for('contact.result'))


@bp.route('/result', methods=('GET', 'POST'))
@login_required
def result():
    contact_list = g.user.contact_set
    return render_template('contact/result.html', contact_list=contact_list)


@bp.route('/resultby', methods=('POST',))
@login_required
def resultby():

    if request.form['ownernum4'] :
        contact_list = Contact.query.filter(and_(Contact.user_id == g.user.id,Contact.ownernum4 == request.form['ownernum4'])).all()
    elif request.form['ownername'] :
        contact_list = Contact.query.filter(and_(Contact.user_id == g.user.id,Contact.ownername == request.form['ownername'])).all()
    else:
        contact_list = Contact.query.filter(and_(Contact.user_id == g.user.id,Contact.ownertel ==request.form['ownertel'])).all()

    return render_template('contact/result.html', contact_list=contact_list)

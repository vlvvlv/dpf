from flask import Blueprint, render_template, url_for, request
from werkzeug.utils import redirect
from mycar import db
from mycar.models import Dpfcar
from sqlalchemy import or_, and_
from mycar.views.auth_views import login_required

bp = Blueprint('dpfcar', __name__, url_prefix='/dpfcar')

@bp.route('/result', methods=('POST',))
@login_required
def result():
    if request.form['carnumber']:
        carnumber = request.form['carnumber']
        carnumin = carnumber[-4:]
        car_num4_01 = carnumber[:-4]+carnumin[0:2] + "**"
        car_num4_02 = carnumber[:-4]+carnumin[0] + "**" + carnumin[3]
        car_num4_03 = carnumber[:-4]+"**" + carnumin[2:4]
        carkind = request.form['carkind']
        if request.form['carkind']:
            dpfcar_list = Dpfcar.query.filter(and_(
                or_(Dpfcar.carnumber == car_num4_01,
                    Dpfcar.carnumber == car_num4_02,
                    Dpfcar.carnumber == car_num4_03),
                Dpfcar.carkind == carkind)).all()
        else:
            dpfcar_list = Dpfcar.query.filter(
                or_(Dpfcar.carnumber == car_num4_01,
                    Dpfcar.carnumber == car_num4_02,
                    Dpfcar.carnumber == car_num4_03)).all()
    else:
        dpfcar_list = ""
    return render_template('search/result.html', dpfcar_list=dpfcar_list)

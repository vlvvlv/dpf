from flask import Blueprint, render_template, url_for, request, flash
from werkzeug.utils import redirect
from werkzeug.utils import secure_filename
import mycar.searchnum
from mycar.models import Dpfcar
from sqlalchemy import or_, and_
from mycar.views.auth_views import login_required
import pandas as pd


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
    return render_template('search/result.html', dpfcar_list=dpfcar_list,carnumber=carnumber ,carkind=carkind)

@bp.route('/img_result', methods=('GET','POST'))
@login_required
def img_result():
    if request.method == 'POST':
        carnumimg= request.files['file'].read()

        # print(secure_filename(f.filename))
        try:
            carnumber = mycar.searchnum.search_num(carnumimg)
        except:
            flash('차량번호 이미지 찾기가 실패하였습니다.')
            # carnumber = ""
            # dpfcar_list = ""
            # return render_template('search/result.html', dpfcar_list=dpfcar_list, carnumber=carnumber)
            return redirect(url_for('dpfcar.go_imgbase'))
        carnumin = carnumber[-4:]
        car_num4_01 = carnumber[:-4]+carnumin[0:2] + "**"
        car_num4_02 = carnumber[:-4]+carnumin[0] + "**" + carnumin[3]
        car_num4_03 = carnumber[:-4]+"**" + carnumin[2:4]

        dpfcar_list = Dpfcar.query.filter(
            or_(Dpfcar.carnumber == car_num4_01,
                Dpfcar.carnumber == car_num4_02,
                Dpfcar.carnumber == car_num4_03)).all()
    else:
        dpfcar_list = ""
    return render_template('search/result.html', dpfcar_list=dpfcar_list,carnumber=carnumber )

@bp.route('/go_base', methods=('GET','POST'))
@login_required
def go_base():
    return render_template('search/base.html')

@bp.route('/go_imgbase', methods=('GET','POST'))
@login_required
def go_imgbase():
    return render_template('search/imgbase.html')

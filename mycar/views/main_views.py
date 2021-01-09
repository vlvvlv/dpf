from flask import Blueprint, render_template
from mycar.views.auth_views import login_required

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
@login_required
def index():
    return render_template('search/base.html')

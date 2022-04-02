import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from app.models.userModels import UserInfo
from app import db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        userId = request.form['userId']
        password = request.form['password']
        error = None

        if not userId:
            error = 'Userid is required.'
        elif not password:
            error = 'Password is required.'
        
        if error is None:
            user_info = UserInfo(
                userId,
                generate_password_hash(password)
            )
            db.session.add(user_info)
            db.session.commit()
            return redirect(url_for("auth.login"))
        
        flash(error)

    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        userId = request.form['userId']
        password = request.form['password']
        
        error = None
        
        user = UserInfo.query.filter_by(userId=userId).first()
        
        if user is None:
            error = 'Incorrect userId.'
        elif not check_password_hash(user.userPassword, password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['userId'] = user.userId
            return "login success!!", 200

        flash(error)

    return render_template('auth/login.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('userId')

    if user_id is None:
        g.user_info = None
    else:
        g.user_info = UserInfo.query.filter_by(userId=user_id).first()

@bp.route('/logout')
def logout():
    session.clear()
    return render_template('auth/login.html')

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user_info is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
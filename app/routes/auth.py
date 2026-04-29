from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user
from app.extensions import login_manager, db, safe_commit
from app.models import User
from app.forms import RegisterForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash


# User loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Blueprint
auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # 1️ Look up user by email
        user = User.query.filter_by(email=form.email.data).first()
        # 2️ Check password
        if not user or not check_password_hash(user.password, form.password.data): # type: ignore
            flash("Invalid email or password", "danger")
            return redirect(url_for('auth.login'))

        # 3️ Log the user in
        login_user(user)
        # 5️ Redirect to home page
        return redirect(url_for('home.portal'))
    # 6️ Render login template with form
    return render_template("auth/login.html", form=form)





@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home.portal'))
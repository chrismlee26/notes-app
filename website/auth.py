# authentication

from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html", boolean=True)


@auth.route('/logout')
def logout():
    return "<p>logout</p>"


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        nickname = request.form.get('nickname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 6:
            flash('That\'s no real email bro', category='error')
        elif len(nickname) < 2:
            flash('You need more than 2 characters', category='error')
        elif password1 != password2:
            flash('passwords should match', category='error')
        elif len(password1) < 7:
            flash('Password should be longer than 7 characters', category='error')
        else:
            new_user = User(email=email, nickname=nickname, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Welcome, account created :O', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html")

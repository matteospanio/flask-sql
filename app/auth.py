from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template("login.html")


@auth.route('/logout')
def logout():
    return render_template("index.html")


@auth.route('/signin')
def sign_in():
    return render_template("signin.html")

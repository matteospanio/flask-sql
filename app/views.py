from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    if method == 'POST':
        return render_template("home.html", name=request.form.get('name'))
    else:
        return render_template("index.html")

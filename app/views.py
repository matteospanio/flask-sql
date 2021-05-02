from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return render_template("home.html", name=request.form.get('name'))

    return render_template("index.html")

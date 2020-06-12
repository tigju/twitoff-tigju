# app/routes/home_routes.py

from flask import Blueprint, render_template
from app.models import User, parse_records  #, db

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    user_records = User.query.all()
    print(user_records)

    users = parse_records(user_records)
    return render_template("prediction_form.html", users=users)


@home_routes.route("/hello")
def hello():
    print("visiting the home page")
    x = 2 + 2
    return f"Hello World! {x}"

@home_routes.route("/about")
def about():
    print("visiting the above page")
    return "About me"

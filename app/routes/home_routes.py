# app/routes/home_routes.py

from flask import Blueprint

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    print("visiting the home page")
    x = 2 + 2
    return f"Hello World! {x}"

@home_routes.route("/about")
def about():
    print("visiting the above page")
    return "About me"

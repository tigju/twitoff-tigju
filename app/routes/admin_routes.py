# app/routes/home_routes.py

from flask import Blueprint, jsonify, render_template, request, flash, redirect

from app.models import db, migrate

import os
from dotenv import load_dotenv
load_dotenv()

admin_routes = Blueprint("admin_routes", __name__)

ADMIN_KEY = os.getenv("ADMIN_KEY")

# GET /admin/db/reset?admin_key=abc123
@admin_routes.route("/admin/db/reset")
def reset_db():
    print("URL PARAMS", dict(request.args))
    
    if request.args["admin_key"] and request.args["admin_key"] == ADMIN_KEY:
        print(type(db))
        db.drop_all()
        db.create_all()
        # return jsonify({"message": "DB RESET COMPLETED"})
        flash("DB RESET COMPLETED", "success")
        return redirect("/")
    else:
        flash("OOPS Permission Denied", "danger")
        return redirect("/")

@admin_routes.route("/admin/db/seed")
def seed_db():
    print(type(db))
    
    # TODO: refactor the existing user and tweet storage logic from our twitter_routes into a re-usable function
    # ... so we can "seed" our database with some example users and tweets
    # ... to ensure that it is ready to make predictions later

    # FYI: you might run into Timeout errors, which you'll need to think about how to avoid
    return jsonify({"message": "DB SEED COMPLETED"})

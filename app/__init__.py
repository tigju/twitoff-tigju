# app/__init__.py
import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv() # loads .env 

from app.models import db, migrate
from app.routes.home_routes import home_routes
from app.routes.book_routes import book_routes
from app.routes.twitter_routes import twitter_routes
from app.routes.stats_routes import stats_routes
from app.routes.admin_routes import admin_routes


DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = "temporary secret value"
def create_app():
    app = Flask(__name__)
    app.static_folder = 'static' # for css

    app.config["SECRET_KEY"] = SECRET_KEY
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)
    app.register_blueprint(twitter_routes)
    app.register_blueprint(stats_routes)
    app.register_blueprint(admin_routes)
    
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)

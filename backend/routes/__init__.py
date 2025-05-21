from .register import register_bp
from flask import Blueprint
from .login import auth_bp

def init_app_routes(app):
    app.register_blueprint(register_bp)
    app.register_blueprint(auth_bp)

from ..routes import auth_bp, register_bp, doacoes_bp, buscar_bp, feed_bp
from flask import Blueprint

def init_app_routes(app):
    app.register_blueprint(register_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(doacoes_bp)
    app.register_blueprint(buscar_bp)
    app.register_blueprint(feed_bp)



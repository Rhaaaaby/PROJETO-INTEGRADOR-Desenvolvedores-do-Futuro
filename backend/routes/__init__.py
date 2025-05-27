from .produtos import produtos_bp
from .register import register_bp 
from .prod_cad import produto_api 
from .doacoes import doacoes_bp
from .buscar import buscar_bp
from .pagina import pages_bp
from .login import auth_bp
from .home import home_bp

def init_app_routes(app):
    app.register_blueprint(produtos_bp)
    app.register_blueprint(register_bp)
    app.register_blueprint(produto_api)
    app.register_blueprint(doacoes_bp)
    app.register_blueprint(buscar_bp)
    app.register_blueprint(pages_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(home_bp)
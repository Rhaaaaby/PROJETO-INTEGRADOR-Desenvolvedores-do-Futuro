from .cadastro_itens import cadastro_itens_bp
from .minha_conta import minha_conta_bp
from .quem_somos import quem_somos_bp
from .register import register_bp 
from .doacoes import doacoes_bp
from .login import auth_bp
from .home import home_bp

def init_app_routes(app):
    app.register_blueprint(cadastro_itens_bp)
    app.register_blueprint(minha_conta_bp)
    app.register_blueprint(quem_somos_bp)
    app.register_blueprint(register_bp)
    app.register_blueprint(doacoes_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(home_bp)
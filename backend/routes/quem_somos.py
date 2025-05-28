from flask import Blueprint, render_template
from jinja2 import TemplateNotFound

quem_somos_bp = Blueprint('quem_somos', __name__)

#QUEM SOMOS 
    
@quem_somos_bp.route("/quem_somos")
def quem_somos():
    try:
        return render_template('quem_somos.html')
    except TemplateNotFound:
        return "Template not found", 404
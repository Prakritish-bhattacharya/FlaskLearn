from flask import Blueprint

blog = Blueprint('blog', __name__)

from blog import routes


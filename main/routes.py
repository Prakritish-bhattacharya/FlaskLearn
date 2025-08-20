# main/routes.py
from flask import Blueprint, render_template   # 1) import Blueprint + templating

# 2) create a Blueprint object
#    first arg: blueprint name (used for url_for endpoint names like "main.index")
#    __name__: tells Flask where this file lives (to locate templates/static)
#    template_folder: folder inside this package where templates are stored
main_bp = Blueprint("main", __name__, template_folder="templates")

# 3) declare a route on the blueprint (NOT on the app)
@main_bp.route("/")                           # responds to GET /
def index():
    # 4) render a template. We namespace it "main/index.html" to avoid name clashes
    return render_template("main/index.html")

# auth/routes.py
from flask import Blueprint, render_template   # 1) imports

# 2) same idea as "main" but this one is named "auth"
auth_bp = Blueprint("auth", __name__, template_folder="templates")

# 3) this route's local path is "/login"
#    Because we registered the blueprint with url_prefix="/auth",
#    the final URL is "/auth/login"
@auth_bp.route("/login")
def login():
    return render_template("auth/login.html")

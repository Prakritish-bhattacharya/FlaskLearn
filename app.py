# app.py
from flask import Flask                       # 1) import Flask core
from main.routes import main_bp               # 2) import the blueprint objects you’ll define
from auth.routes import auth_bp               # 3) (one for auth)

app = Flask(__name__)                         # 4) create the real Flask app

# 5) register the "main" blueprint at root URLs
#    Any route declared in main_bp (like "/") is now available at "/"
app.register_blueprint(main_bp)

# 6) register the "auth" blueprint under a URL prefix
#    A route declared as "/login" in auth_bp becomes "/auth/login"
app.register_blueprint(auth_bp, url_prefix="/auth")

# 7) development entrypoint: run with reloader and debugger
if __name__ == "__main__":
    app.run(debug=True)

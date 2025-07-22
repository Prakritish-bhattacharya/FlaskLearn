from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import render_template
from flask import request

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<h1>Hey Prakritish, welcome from Flask end</h1>"

# @app.route("/")
# def index():
#     return "<p>Index Page</p>"

# @app.route("/hello")
# def hello():
#     return "<p>Hello Page</p>"

# @app.route("/<name>")
# def helloEscape(name):
#     return f"<h1>Hello, {escape(name)}</h1>"

# @app.route("/user/<username>")
# def show_user_profile(username):
#     # show the user profile for that user
#     return f"<h1>user {escape(username)}</h1>"

# @app.route("/post/<int:post_id>")
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return f"Post {post_id}"

# @app.route("/path/<path:subpath>")
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return f"<h1>subpath {escape(subpath)}</h1>"


# URL Building
# @app.route('/')
# def index():
#     return 'index'

# @app.route('/login')
# def login():
#     return 'login'

# @app.route('/user/<username>')
# def profile(username):
#     return f'{username}\'s profile'

# with app.test_request_context():
#     print(url_for('index'))  # prints: /
#     print(url_for('login'))  # prints: /login
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))  # prints: /user/John
# @app.route('/')
# def index():
#     return '<p>This is the home page. Go to <a href="/hello/">/hello/</a></p>'


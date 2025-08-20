import app
from blog import blog

@app.route('/blog')
def blog():
    return "Blog Home Page"
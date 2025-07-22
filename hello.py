from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("txtName", "").strip()
        email = request.form.get("txtEmail", "").strip()
        mobile = request.form.get("txtMobile", "").strip()
        
        # simple validation rule
        if not name or not email or not mobile:
            return render_template(
                "form.html",
                error = "All fileds are required.",
                old={"txtName": name, "txtEmail": email, "txtMobile": mobile}
            )
            
        if "@" not in email:
            return render_template(
                "form.html",
                error = "Invalid email address.",
                old={"txtName": name, "txtEmail": email, "txtMobile": mobile}
            )

# Success
        collect = {"Name": name, "Email": email, "Mobile": mobile}
        return render_template("success.html", data=collect)

    # GET request: show blank form
    return render_template("form.html", error=None, old=None)
        
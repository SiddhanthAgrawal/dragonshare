
from flask import *
from flask_cors import CORS
from app.utils.db import *

app = Flask(__name__)
app.secret_key = "hjsdfhjksdfhksdfjkln"
CORS(app)

@app.route("/", methods=["GET"])
def home():
    if "email" in session:
        return render_template("home.html")
    else:
        return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        email = request.form["email"]
        password = request.form["password"]
        users = User.objects(email=email)
        if len(users) == 0:
            flash("invalid credentials")
            return redirect("/login")
        session["email"] = email
        return redirect("/")

@app.route("/logout", methods=["GET"])
def logout():
    session.pop("email")
    return redirect("/login")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        print("got here")
        email = request.form["email"]
        pw0 = request.form["password0"]
        pw1 = request.form["password1"]
                
        if (email.split("@")[-1] != "drexel.edu"):
            flash("You need a Drexel Email")
            return render_template("register.html")
        
        if (pw0 != pw1):
            flash("passwords must match")
            return render_template("register.html")
        session["email"] = email
        User(email=email, password=pw0).save()
        return redirect("/")

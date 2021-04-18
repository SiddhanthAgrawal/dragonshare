
from flask import *
from flask_cors import CORS
from app.utils.db import *
from random import randint

app = Flask(__name__)
app.secret_key = "hjsdfsdsddfhksdfjksdfln"
CORS(app)

@app.route("/", methods=["GET"])
def home():
    if "email" in session:
        
        return render_template("Postpage.html", data=Post.objects())
    else:
        return render_template("index.html")


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
    return redirect("/")

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

@app.route("/newpost", methods=["GET", "POST"])
def newPost():
    if request.method == "GET":
        return render_template("form.html")
    data = request.form.to_dict()

    Post(name=data["name"], start=data["from"], to=data["to"], 
        contact=data["phone"], gender=data["gender"], no=data["no"], 
        child=data["child"], idNo=randint(11111111, 99999999)).save()
    return redirect("/")

@app.route("/postdelete/<int:postid>", methods=["POST"])
def deletePost(postid):
    Post.objects(idNo=postid)[0].delete()
    return redirect("/")
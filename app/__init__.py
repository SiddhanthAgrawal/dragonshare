
from flask import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        pass

@app.route("/register")
def register():
    return render_template("register.html")
    
    pass
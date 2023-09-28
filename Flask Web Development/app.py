from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SECRET_KEY"] = "abc"
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.init_app(app)


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    email = db.Column(db.String(30))
    password = db.Column(db.String(20))


db.init_app(app)

with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = Users.query.filter_by(email=request.form.get("email")).first()
        if user:
            return redirect(url_for("login"))

        else:
            user = Users(username=request.form.get("username"), email=request.form.get(
                "email"), password=request.form.get("password"))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("login"))
    else:
        if current_user.is_authenticated:
             return redirect(url_for("home"))
        return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = Users.query.filter_by(
            email=request.form.get("email")).first()
        if user:
            if user.password == request.form.get("password"):
                login_user(user)
                return redirect(url_for("home"))
            else:
                return redirect(url_for("login"))
        else:
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask,redirect,url_for,render_template

app = Flask(__name__)
# @app.route("/")
# def home():
#     return "hello <h1> in line HTML <p> ahhh</p>"
# @app.route("/admin")
# def admin():
#     return redirect(url_for("home"))

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()

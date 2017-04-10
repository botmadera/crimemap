from dbhelper import DBHelper
from flask import Flask
from flask import render_template

app = Flask(__name__)

DB = DBHelper()

@app.route("/")
def home():
    try:
        data = DB.get_all_inputs()

    except Exception as e:
        print e
        data = None
    return render_template("home.html", data = data)

@app.route("/clear")
def clear():
    try:
        DB.clear_all()
    except Exception as e:
        print e
    return home()

if __name__ == '__main__':
    app.run()
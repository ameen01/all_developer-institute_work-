from app import app
from flask import render_template



@app.route("/")
def homepage():

    return render_template("wep.html")


@app.route('/add', methods=['GET', 'POST'])
def add_page():

    render_template()
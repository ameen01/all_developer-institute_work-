from website import app
import flask
import os
import random


@app.route("/")
@app.route("/home")
def home():

    return flask.render_template("am@@n&cile♦♥.html")


@app.route("/tv_show")
def tv_show():

    return flask.render_template("video.html")


@app.route("/movies")
def movies():
    return flask.render_template("am@@n&cile♦♥.html")


@app.route("/python")
def python():
    return flask.render_template("am@@n&cile♦♥.html")


@app.route("/music")
def music():
    return flask.render_template("music.html")
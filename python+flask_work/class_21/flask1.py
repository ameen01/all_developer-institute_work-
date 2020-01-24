import flask
import datetime
import random

app = flask.Flask("my_app")


@app.route("/like")
@app.route("/home")
def first_view():
    my_name = "adam"
    now = datetime.datetime.now()
    time = "{}/{}/{}".format(now.day, now.month, now.year)
    secend = datetime.time
    rendr = flask.render_template("te.html", name=my_name, time=time
                                  , sea=secend)
    return rendr


@app.route("/<int:num>")
def welc(num):
    number = random.randrange(1, 10)
    if num == number:
        return "your number is" + number
    else:
        return "number not match"


@app.route("/me")
def sec_view():
    t2 = flask.render_template("t2", )
    return t2


if __name__ == "__main__":
    app.run(port=5000)

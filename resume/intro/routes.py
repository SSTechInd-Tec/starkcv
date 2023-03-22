from flask import Blueprint, render_template, url_for


resume_b = Blueprint("resume", __name__)


@resume_b.route("/")
def home():
    return render_template("intro/home.html")

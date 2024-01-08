from flask import Blueprint, render_template

views = Blueprint('views', __name__, template_folder="temps")

@views.route('/')
def home():
	return render_template("home.html")
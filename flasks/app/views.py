# app/views.py

from flask import render_template

from app import app

# route to main page
@app.route('/')
def index():
	return render_template("index.html")

# route to about page
@app.route('/about')
def about():
	return render_template("about.html")

# route to test page
@app.route('/test')
def test():
	return render_template("test.html")
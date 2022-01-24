from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo_model import Dojo

@app.route('/')
def root():
    return render_template("index.html")

@app.route('/form', methods=["POST"])
def form():

    if not Dojo.validate_ninja(request.form):
        return redirect("/")

    data = {
        'name' : request.form['name'],
        'd_location' : request.form['d_location'],
        'language' : request.form['language'],
        'comments' : request.form['comments'],
        'id' : request.form['id']
    }

    Dojo.save(data)
    return redirect("/results")

@app.route('/results')
def results():
    dojo = Dojo.get_all()
    return render_template("results.html", dojo = dojo)
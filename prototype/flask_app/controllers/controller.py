from flask import render_template, redirect
from flask_app import app


@app.route('/')
def redirectGEThome():
    # if 'userid' in session:
    #     return redirect('/dashboard')
    return redirect('/home')

@app.route('/home')
def GEThome():
    return render_template('home.html')

@app.route('/dashboard')
def GETdashboard():
    # if 'userid' not in session:
    #     return redirect('/home')
    return render_template('dashboard.html')

@app.route('/about')
def GETabout():
    # if 'userid' not in session:
    #     return redirect('/home')
    return render_template('about.html')

@app.route('/mint')
def GETmint():
    # if 'userid' not in session:
    #     return redirect('/home')
    return render_template('mint.html')

@app.route('/customize')
def GETcustomize():
    # if 'userid' not in session:
    #     return redirect('/home')
    return render_template('customize.html')
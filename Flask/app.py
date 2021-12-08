from re import A
from flask import Flask, request, render_template, url_for, redirect, session, g
from flask_sqlalchemy import SQLAlchemy

import pickle, os

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

@app.route('/')
def index():
    return render_template("login.html")
database={'abc':'123'}

@app.route('/form_login',methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    if name1 not in database:
        return render_template('login.html', info='Invalid User')
    else:
        if database[name1]!=pwd:
            return render_template('login.html', info='Invalid Password')
        else:
             return render_template('options.html')


@app.route('/selection')
def selection():
        return render_template('options.html')

@app.route('/scheduler')
def scheduler():
    return render_template('todolist.html')

@app.route('/sets')
def sets():
    return render_template('Sets.html')

@app.route('/unitOne')
def unitone():
    return render_template('res_Allo.html')

@app.route('/unitTwo')
def unittwo():
    return render_template('price_Sys.html')

@app.route('/unitThree')
def unitthree():
    return render_template('govt_Micro.html')

@app.route('/unitFour')
def unitfour():
    return render_template('mac_Econ.html')

@app.route('/unitFive')
def unitfive():
    return render_template('govt_Macro.html')

if __name__ == '__main__':
    #db.create_all()
    app.run(debug=True)
from re import A
from flask import Flask,request,render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import pickle

app = Flask(__name__)
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
database={'DKothari':'DK200304'}

@app.route('/form_login',methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    if name1 not in database:
	    return render_template('login.html',info='Invalid User')
    else:
        if database[name1]!=pwd:
            return render_template('login.html',info='Invalid Password')
        else:
	         return render_template('Sets.html')

@app.route("/schedule")
def schedule():
    #todo_list = Todo.query.all()
    return render_template("schedule.html")
    
#@app.route("/add", methods=["POST"])
#def add():
#    title = request.form.get("title")
#   new_todo = Todo(title=title, complete=False)
#    db.session.add(new_todo)
#    db.session.commit()
#    return redirect(url_for("schedule"))


#@app.route("/update/<int:todo_id>")
#def update(todo_id):
#    todo = Todo.query.filter_by(id=todo_id).first()
#    todo.complete = not todo.complete
#    db.session.commit()
#    return redirect(url_for("schedule"))


#@app.route("/delete/<int:todo_id>")
#ef delete(todo_id):
#    todo = Todo.query.filter_by(id=todo_id).first()
#    db.session.delete(todo)
#    db.session.commit()
#    return redirect(url_for("schedule"))

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
    app.run()
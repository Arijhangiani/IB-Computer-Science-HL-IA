from flask import Flask,request,render_template
import pickle

app = Flask(__name__)

@app.route('/')
def hello_world():
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
    app.run()
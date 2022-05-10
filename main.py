from flask import Flask
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def head():
    return "OK"

@app.route('/home',methods=['GET','POST'])
def head():
    return "home"


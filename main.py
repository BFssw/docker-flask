from flask import Flask
from flask_gzip import Gzip


app = Flask(__name__)
gzip = Gzip(app)


@app.route('/',methods=['GET','POST'])
def head():
    return "OK"

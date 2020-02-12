from flask import Flask, render_template, request, url_for,session
from werkzeug.utils import redirect
import json

app=Flask(__name__)
app.secret_key=b'Pa$$w0rd'

@app.route('/')
def inicio():
    return render_template('index.html')






if __name__=='__main__':
    app.run(debug=True)
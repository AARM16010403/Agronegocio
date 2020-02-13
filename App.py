from flask import Flask, render_template, request, url_for,session
from werkzeug.utils import redirect
import json

app=Flask(__name__)
app.secret_key=b'Pa$$w0rd'

@app.route('/')
def inicio():
    return render_template('index.html')
@app.route('/login',methods=['POST'])
def login():
    u=request.form['usuario']
    c=request.form['contra']
    if u=='Juan':
        if c=='qwerty':
            return render_template('Ventas/Principal.html')


if __name__=='__main__':
    app.run(debug=True)
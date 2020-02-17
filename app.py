from flask import Flask, render_template, request, url_for, session
from werkzeug.utils import redirect

from Datoss.CultivosDAO import CultivosDAO
from Datoss.AsociacionesDAO import AsociacionesDAO
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
        else:
            return render_template('index.html')
    else:
        return render_template('index.html')
@app.route('/cultivos')
def cultivos():
    cdao = CultivosDAO()
    lista = cdao.obtenerCultivos()
    return render_template('Ventas/Cultivos.html', cultivos=lista, user=session.get('user'))
@app.route('/asociacion')
def asociaciones():
    adao = AsociacionesDAO()
    lista = adao.obtenerAsociaciones()
    return render_template('Ventas/Asociaciones.html', asociaciones=lista, user=session.get('user'))

if __name__=='__main__':
    app.run(debug=True)
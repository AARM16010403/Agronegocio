from flask import Flask, render_template, request, url_for, session
from werkzeug.utils import redirect

from Datoss.ClientesDAO import ClientesDAO
from Datoss.CultivosDAO import CultivosDAO
from Datoss.AsociacionesDAO import AsociacionesDAO
from Datoss.UnidadesTransDAO import UnidadesTransDAO
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
@app.route('/unidades')
def unidades():
    udao = UnidadesTransDAO()
    lista = udao.obtenerUnidades()
    return render_template('Ventas/UnidadesTrans.html', unidades=lista, user=session.get('user'))
@app.route('/clientes')
def clientes():
    cdao = ClientesDAO()
    lista = cdao.obtenerClientes()
    return render_template('Ventas/Clientes.html', clientes=lista, user=session.get('user'))

if __name__=='__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, url_for, session
from werkzeug.utils import redirect

from Datoss.ClientesDAO import ClientesDAO
from Datoss.Conexion import Conexion
from Datoss.CultivosDAO import CultivosDAO
from Datoss.AsociacionesDAO import AsociacionesDAO
from Datoss.MiembrosDAO import MiembrosDAO
from Datoss.UnidadesTransDAO import UnidadesTransDAO
import json
import pyodbc

from Modelo.Asociacion import Asociacion
from Modelo.Cliente import Cliente
from Modelo.Cultivo import Cultivo
<<<<<<< HEAD
from Modelo.Miembro import Miembro
=======
>>>>>>> d070e01b60ecf41de2efd276acde0aac9b6a9dc0
from Modelo.UnidadTrans import UnidadTrans

app=Flask(__name__)
app.secret_key=b'Pa$$w0rd'

@app.route('/')
def inicio():
    return render_template('index.html')
@app.route('/login',methods=['POST'])
def login():
    u=request.form['usuario']
    c=request.form['contra']
    conx = Conexion()
    db = conx.getDB()
    sql = 'select nombre,contrasenia from Seguridad.Usuarios'
    cursor = db.cursor()
    cursor.execute(sql);
    data = cursor.fetchall()
    entrar = False
    for dato in data:
        if dato[0] == u:
            if dato[1] == c:
                entrar = True
    cursor.close()
    db.close()
    if entrar:
        session['user'] = u
        return render_template('Ventas/Principal.html',user=session.get('user'))
    else:
        return render_template('index.html')
@app.route('/ventas')
def ventas():
<<<<<<< HEAD
    return render_template('Ventas/Principal.html',user=session.get('user'))
=======
    return render_template('Ventas/Principal.html')
>>>>>>> d070e01b60ecf41de2efd276acde0aac9b6a9dc0
@app.route('/cultivos')
def cultivos():
    cdao = CultivosDAO()
    lista = cdao.obtenerCultivos()
    return render_template('Ventas/Cultivos.html', cultivos=lista, user=session.get('user'))
@app.route('/nuevoCultivo')
def nuevocultivo():
    cdao = CultivosDAO()
    id = cdao.ultimoID()
    return render_template('Ventas/Insertar/agregarCultivo.html', id=id, user=session.get('user'))
@app.route('/agregarCultivo',methods=['POST'])
def agregarcultivo():
    cultivo = Cultivo(request.form['id'],request.form['nombre'],request.form['costo'],'A')
    cdao = CultivosDAO()
    cdao.insertarCultivo(cultivo)
    return redirect(url_for('cultivos'))
@app.route('/consultarCultivo/<id>')
def consultarCultivo(id):
    cdao = CultivosDAO()
    c=cdao.consultaIndividual(id)
    return render_template('Ventas/Editar/editarCultivo.html',cultivo=c,user=session.get('user'))
@app.route('/editarCultivo',methods=['POST'])
def actualizarCultivo():
    c = Cultivo(request.form['id'],request.form['nombre'],request.form['costo'],'A')
    cdao = CultivosDAO()
    cdao.actualizar(c)
    return redirect(url_for('cultivos'))
@app.route('/eliminarCultivo/<id>')
def eliminarCultivo(id):
    cdao = CultivosDAO()
    cdao.eliminar(id)
    return redirect(url_for('cultivos'))
@app.route('/asociacion')
def asociaciones():
    adao = AsociacionesDAO()
    lista = adao.obtenerAsociaciones()
    return render_template('Ventas/Asociaciones.html', asociaciones=lista, user=session.get('user'))
@app.route('/nuevaAsociacion')
def nuevaAsociacion():
    adao = AsociacionesDAO()
    id = adao.ultimoID()
    return render_template('Ventas/Insertar/agregarAsociaciones.html', id=id, user=session.get('user'))
@app.route('/agregarAsociacion',methods=['POST'])
def agregarasociacion():
    asociacion = Asociacion(request.form['id'],request.form['nombre'],'A')
    adao = AsociacionesDAO()
    adao.insertarAsociacion(asociacion)
    return redirect(url_for('asociaciones'))
@app.route('/consultarAsociacion/<id>')
def consultarAsociacion(id):
    adao = AsociacionesDAO()
    a=adao.consultaIndividual(id)
    return render_template('Ventas/Editar/editarAsociaciones.html',asociacion=a,user=session.get('user'))
@app.route('/editarAsociacion',methods=['POST'])
def actualizarAsociacion():
    a = Asociacion(request.form['id'],request.form['nombre'],'A')
    adao = AsociacionesDAO()
    adao.actualizar(a)
    return redirect(url_for('asociaciones'))
@app.route('/eliminarAsociacion/<id>')
def eliminarAsociacion(id):
    adao = AsociacionesDAO()
    adao.eliminar(id)
    return redirect(url_for('asociaciones'))
@app.route('/unidades')
def unidades():
    udao = UnidadesTransDAO()
    lista = udao.obtenerUnidades()
    return render_template('Ventas/UnidadesTrans.html', unidades=lista, user=session.get('user'))
@app.route('/nuevaUnidad')
def nuevaUnidad():
    udao = UnidadesTransDAO()
    id = udao.ultimoID()
    return render_template('Ventas/Insertar/agregarUnidades.html', id=id, user=session.get('user'))
@app.route('/agregarUnidad',methods=['POST'])
def agregarUnidad():
    unidad = UnidadTrans(request.form['id'],request.form['placa'],request.form['marca'],request.form['modelo']
                         ,request.form['anio'],request.form['capacidad'],'A')
    udao = UnidadesTransDAO()
    udao.insertarUnidad(unidad)
    return redirect(url_for('unidades'))
@app.route('/consultarUnidad/<id>')
def consultarUnidad(id):
    udao = UnidadesTransDAO()
    u=udao.consultaIndividual(id)
    return render_template('Ventas/Editar/editarUnidad.html',unidad=u,user=session.get('user'))
@app.route('/editarUnidad',methods=['POST'])
def actualizarUnidad():
    u = UnidadTrans(request.form['id'],request.form['placa'],request.form['marca'],request.form['modelo']
<<<<<<< HEAD
                    ,request.form['anio'],request.form['capacidad'],'A')
=======
                         ,request.form['anio'],request.form['capacidad'],'A')
>>>>>>> d070e01b60ecf41de2efd276acde0aac9b6a9dc0
    udao = UnidadesTransDAO()
    udao.actualizar(u)
    return redirect(url_for('unidades'))
@app.route('/eliminarUnidad/<id>')
def eliminarUnidad(id):
    udao = UnidadesTransDAO()
    udao.eliminar(id)
    return redirect(url_for('unidades'))
@app.route('/clientes')
def clientes():
    cdao = ClientesDAO()
    lista = cdao.obtenerClientes()
    return render_template('Ventas/Clientes.html', clientes=lista, user=session.get('user'))
@app.route('/nuevoCliente')
def nuevoCliente():
    cdao = ClientesDAO()
    id = cdao.ultimoID()
    conx = Conexion()
    db = conx.getDB()
    lista = []
    sql = 'select idCiudad,nombre from RH.Ciudades'
    cursor = db.cursor()
    cursor.execute(sql);
    data = cursor.fetchall()
    for dato in data:
        fila = {"id":dato[0],"nombre":dato[1]}
        lista.append(fila)
    cursor.close()
    db.close()
    return render_template('Ventas/Insertar/agregarCliente.html', id=id,ciudades=lista, user=session.get('user'))
@app.route('/agregarCliente',methods=['POST'])
def agregarCliente():
    cliente = Cliente(request.form['id'],request.form['nombre'],request.form['razon'],request.form['limite']
                         ,request.form['direccion'],request.form['codigo'],request.form['rfc'],request.form['telefono'],
                      request.form['email'],request.form['tipo'],request.form['ciudad'],'A')
    cdao = ClientesDAO()
    cdao.insertarCliente(cliente)
    return redirect(url_for('clientes'))
@app.route('/consultarCliente/<id>')
def consultarCliente(id):
    cdao = ClientesDAO()
    c=cdao.consultaIndividual(id)
    conx = Conexion()
    db = conx.getDB()
    lista = []
    sql = 'select idCiudad,nombre from RH.Ciudades'
    cursor = db.cursor()
<<<<<<< HEAD
    cursor.execute(sql)
=======
    cursor.execute(sql);
>>>>>>> d070e01b60ecf41de2efd276acde0aac9b6a9dc0
    data = cursor.fetchall()
    for dato in data:
        fila = {"id": dato[0], "nombre": dato[1]}
        lista.append(fila)
    cursor.close()
    db.close()
    return render_template('Ventas/Editar/editarCliente.html',cliente=c,ciudades=lista,user=session.get('user'))
@app.route('/editarCliente',methods=['POST'])
def actualizarCliente():
    c = Cliente(request.form['id'],request.form['nombre'],request.form['razon'],request.form['limite']
                         ,request.form['direccion'],request.form['codigo'],request.form['rfc'],request.form['telefono'],
                      request.form['email'],request.form['tipo'],request.form['ciudad'],'A')
    cdao = ClientesDAO()
    cdao.actualizar(c)
    return redirect(url_for('clientes'))
@app.route('/eliminarCliente/<id>')
def eliminarCliente(id):
    cdao = ClientesDAO()
    cdao.eliminar(id)
    return redirect(url_for('clientes'))
<<<<<<< HEAD
@app.route('/miembros')
def miembros():
    mdao = MiembrosDAO()
    lista = mdao.obtenerMiembros()
    return render_template('Ventas/Miembros.html', miembros=lista, user=session.get('user'))
@app.route('/nuevoMiembro')
def nuevoMiembro():
    mdao = MiembrosDAO()
    conx = Conexion()
    db = conx.getDB()
    lista1 = []
    lista2 = []
    sql = "select idCliente,nombre from Ventas.Clientes where estatus='A'"
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    for dato in data:
        fila = {"id": dato[0], "nombre": dato[1]}
        lista1.append(fila)
    sql = "select idAsociacion,nombre from Ventas.Asociaciones where estatus='A'"
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    for dato in data:
        fila = {"id": dato[0], "nombre": dato[1]}
        lista2.append(fila)
    cursor.close()
    db.close()
    return render_template('Ventas/Insertar/agregarMiembro.html',clientes=lista1,asociaciones=lista2, user=session.get('user'))
@app.route('/agregarMiembro',methods=['POST'])
def agregarMiembro():
    f = request.form['fechaIncorporacion']
    print (f)
    f = f[0:10]
    print (f)
    m = Miembro(request.form['idCliente'],request.form['idAsociacion'],'A',f)
    mdao = MiembrosDAO()
    mdao.insertarMiembro(m)
    return redirect(url_for('miembros'))
@app.route('/consultarMiembro/<idC>/<idA>')
def consultarMiembro(idC,idA):
    mdao = MiembrosDAO()
    print(idC)
    m=mdao.consultaIndividual(idC,idA)
    conx = Conexion()
    db = conx.getDB()
    lista1 = []
    lista2 = []
    sql = "select idCliente,nombre from Ventas.Clientes where estatus='A'"
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    for dato in data:
        fila = {"id": str(dato[0]), "nombre": dato[1]}
        lista1.append(fila)
    sql = "select idAsociacion,nombre from Ventas.Asociaciones where estatus='A'"
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    for dato in data:
        fila = {"id": str(dato[0]), "nombre": dato[1]}
        lista2.append(fila)
    cursor.close()
    db.close()
    return render_template('Ventas/Editar/editarMiembro.html',miembro=m,clientes=lista1,asociaciones=lista2,idC=idC,idA=idA,user=session.get('user'))
@app.route('/editarMiembro/<idC>/<idA>',methods=['POST'])
def actualizarMiembro(idC,idA):
    f = request.form['fechaIncorporacion']
    print (f)
    f = f[0:10]
    print (f)
    m = Miembro(request.form['idCliente'],request.form['idAsociacion'],'A',f)
    mdao = MiembrosDAO()
    mdao.actualizar(m,idC,idA)
    return redirect(url_for('miembros'))
@app.route('/eliminarMiembro/<idC>/<idA>')
def eliminarMiembro(idC,idA):
    mdao = MiembrosDAO()
    mdao.eliminar(idC,idA)
    return redirect(url_for('miembros'))
=======
>>>>>>> d070e01b60ecf41de2efd276acde0aac9b6a9dc0

if __name__=='__main__':
    app.run(debug=True)
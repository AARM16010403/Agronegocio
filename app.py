from flask import Flask, render_template, request, url_for, session
from werkzeug.utils import redirect

from Datoss.ClientesCultivosDAO import ClientesCultivosDAO
from Datoss.ClientesDAO import ClientesDAO
from Datoss.Conexion import Conexion
from Datoss.CultivosDAO import CultivosDAO
from Datoss.AsociacionesDAO import AsociacionesDAO
from Datoss.MiembrosDAO import MiembrosDAO
<<<<<<< Updated upstream
=======
from Datoss.OfertasAsociacionDAO import OfertasAsociacionDAO
from Datoss.OfertasDAO import OfertasDAO
>>>>>>> Stashed changes
from Datoss.UnidadesTransDAO import UnidadesTransDAO
import json
import pyodbc

from Modelo.Asociacion import Asociacion
from Modelo.Cliente import Cliente
<<<<<<< Updated upstream
<<<<<<< Updated upstream
from Modelo.Cultivo import Cultivo
<<<<<<< Updated upstream
<<<<<<< HEAD
from Modelo.Miembro import Miembro
=======
>>>>>>> d070e01b60ecf41de2efd276acde0aac9b6a9dc0
=======
from Modelo.Miembro import Miembro
>>>>>>> Stashed changes
=======
from Modelo.ClienteCultivo import ClienteCultivo
from Modelo.Cultivo import Cultivo
from Modelo.Miembro import Miembro
>>>>>>> Stashed changes
=======
from Modelo.ClienteCultivo import ClienteCultivo
from Modelo.Cultivo import Cultivo
from Modelo.Miembro import Miembro
from Modelo.Oferta import Oferta
from Modelo.OfertaAsociacion import OfertaAsociacion
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
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
=======
    res = conx.verificarUsuario(u,c)
    if res:
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
>>>>>>> Stashed changes
    else:
        return render_template('index.html')
@app.route('/ventas')
def ventas():
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< HEAD
    return render_template('Ventas/Principal.html',user=session.get('user'))
=======
    return render_template('Ventas/Principal.html')
>>>>>>> d070e01b60ecf41de2efd276acde0aac9b6a9dc0
=======
    return render_template('Ventas/Principal.html',user=session.get('user'))
>>>>>>> Stashed changes
=======
    return render_template('Ventas/Principal.html',user=session.get('user'))
>>>>>>> Stashed changes
=======
    return render_template('Ventas/Principal.html',user=session.get('user'))
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< HEAD
                    ,request.form['anio'],request.form['capacidad'],'A')
=======
                         ,request.form['anio'],request.form['capacidad'],'A')
>>>>>>> d070e01b60ecf41de2efd276acde0aac9b6a9dc0
=======
                    ,request.form['anio'],request.form['capacidad'],'A')
>>>>>>> Stashed changes
=======
                    ,request.form['anio'],request.form['capacidad'],'A')
>>>>>>> Stashed changes
=======
                    ,request.form['anio'],request.form['capacidad'],'A')
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< HEAD
    cursor.execute(sql)
=======
    cursor.execute(sql);
>>>>>>> d070e01b60ecf41de2efd276acde0aac9b6a9dc0
=======
    cursor.execute(sql)
>>>>>>> Stashed changes
=======
    cursor.execute(sql)
>>>>>>> Stashed changes
=======
    cursor.execute(sql)
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< HEAD
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
=======
>>>>>>> d070e01b60ecf41de2efd276acde0aac9b6a9dc0
=======
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
@app.route('/clientesCultivos')
def clientesCultivos():
    ccdao = ClientesCultivosDAO()
    lista = ccdao.obtenerClientesCultivos()
    return render_template('Ventas/ClientesCultivos.html', clientescultivos=lista, user=session.get('user'))
<<<<<<< Updated upstream
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
@app.route('/nuevoClienteCultivo')
def nuevoClienteCultivo():
    ccdao = ClientesCultivosDAO()
=======
@app.route('/nuevoClienteCultivo')
def nuevoClienteCultivo():
    ccdao = ClientesCultivosDAO()
    id = ccdao.ultimoID()
>>>>>>> Stashed changes
    conx = Conexion()
    db = conx.getDB()
    lista1 = []
    lista2 = []
    lista3 = []
    sql = "select idCliente,nombre from Ventas.Clientes where estatus='A'"
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    for dato in data:
        fila = {"id": str(dato[0]), "nombre": dato[1]}
        lista1.append(fila)
    sql = "select idCultivo,nombre from Ventas.Cultivos where estatus='A'"
    cursor.execute(sql)
    data = cursor.fetchall()
    for dato in data:
        fila = {"id": str(dato[0]), "nombre": dato[1]}
        lista2.append(fila)
    sql = "select idCiudad,nombre from RH.Ciudades"
    cursor.execute(sql)
    data = cursor.fetchall()
    for dato in data:
        fila = {"id": str(dato[0]), "nombre": dato[1]}
        lista3.append(fila)
    cursor.close()
    db.close()
<<<<<<< Updated upstream
    return render_template('Ventas/Insertar/agregarClienteCultivo.html',clientes=lista1,cultivos=lista2,ciudades=lista3, user=session.get('user'))
@app.route('/agregarClienteCultivo',methods=['POST'])
def agregarClienteCultivo():
    cc = ClienteCultivo(request.form['idClienteCultivo'],request.form['extension'],request.form['ubicacion'],request.form['idCliente'],
=======
    return render_template('Ventas/Insertar/agregarClienteCultivo.html',id=id,clientes=lista1,cultivos=lista2,ciudades=lista3, user=session.get('user'))
@app.route('/agregarClienteCultivo',methods=['POST'])
def agregarClienteCultivo():
    cc = ClienteCultivo(request.form['id'],request.form['extension'],request.form['ubicacion'],request.form['idCliente'],
>>>>>>> Stashed changes
                request.form['idCultivo'],request.form['idCiudad'],'A')
    ccdao = ClientesCultivosDAO()
    ccdao.insertarClienteCultivo(cc)
    return redirect(url_for('clientesCultivos'))
@app.route('/consultarClienteCultivo/<id>/<idC>/<idCu>/<idCi>')
<<<<<<< Updated upstream
def consultarMiembro(id,idC,idCu,idCi):
=======
def consultarClienteCultivo(id,idC,idCu,idCi):
>>>>>>> Stashed changes
    ccdao = ClientesCultivosDAO()
    cc = ccdao.consultaIndividual(id)
    conx = Conexion()
    db = conx.getDB()
    lista1 = []
    lista2 = []
    lista3 = []
    sql = "select idCliente,nombre from Ventas.Clientes where estatus='A'"
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    for dato in data:
<<<<<<< Updated upstream
        fila = {"id": dato[0], "nombre": dato[1]}
=======
        fila = {"id": str(dato[0]), "nombre": dato[1]}
>>>>>>> Stashed changes
        lista1.append(fila)
    sql = "select idCultivo,nombre from Ventas.Cultivos where estatus='A'"
    cursor.execute(sql)
    data = cursor.fetchall()
    for dato in data:
<<<<<<< Updated upstream
        fila = {"id": dato[0], "nombre": dato[1]}
=======
        fila = {"id": str(dato[0]), "nombre": dato[1]}
>>>>>>> Stashed changes
        lista2.append(fila)
    sql = "select idCiudad,nombre from RH.Ciudades"
    cursor.execute(sql)
    data = cursor.fetchall()
    for dato in data:
<<<<<<< Updated upstream
        fila = {"id": dato[0], "nombre": dato[1]}
=======
        fila = {"id": str(dato[0]), "nombre": dato[1]}
>>>>>>> Stashed changes
        lista3.append(fila)
    cursor.close()
    db.close()
    return render_template('Ventas/Editar/editarClienteCultivo.html',clienteCultivo=cc,clientes=lista1,cultivos=lista2,ciudades=lista3,
                           idC=idC,idCu=idCu,idCi=idCi,user=session.get('user'))
@app.route('/editarClienteCultivo',methods=['POST'])
def editarClienteCultivo():
<<<<<<< Updated upstream
    cc = ClienteCultivo(request.form['idClienteCultivo'],request.form['extension'],request.form['ubicacion'],request.form['idCliente'],
=======
    cc = ClienteCultivo(request.form['id'],request.form['extension'],request.form['ubicacion'],request.form['idCliente'],
>>>>>>> Stashed changes
                request.form['idCultivo'],request.form['idCiudad'],'A')
    ccdao = ClientesCultivosDAO()
    ccdao.actualizar(cc)
    return redirect(url_for('clientesCultivos'))
@app.route('/eliminarClienteCultivo/<id>')
def eliminarClienteCultivo(id):
    ccdao = ClientesCultivosDAO()
    ccdao.eliminar(id)
    return redirect(url_for('clientesCultivos'))
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
@app.route('/ofertas')
def ofertas():
    odao = OfertasDAO()
    lista = odao.obtenerOfertas()
    return render_template('Ventas/Ofertas.html', ofertas=lista, user=session.get('user'))
@app.route('/nuevaOferta')
def nuevaOferta():
    odao = OfertasDAO()
    id = odao.ultimoID()
    conx = Conexion()
    db = conx.getDB()
    lista = []
    sql = 'select idProducto,nombre from Compras.Productos'
    cursor = db.cursor()
    cursor.execute(sql);
    data = cursor.fetchall()
    for dato in data:
        fila = {"id":dato[0],"nombre":dato[1]}
        lista.append(fila)
    cursor.close()
    db.close()
    return render_template('Ventas/Insertar/agregarOferta.html', id=id,productos=lista, user=session.get('user'))
@app.route('/agregarOferta',methods=['POST'])
def agregarOferta():
    o = Oferta(request.form['id'],request.form['nombre'],request.form['descripcion'],request.form['descuento'],
                request.form['fechaInicio'],request.form['fechaFin'],request.form['canMinProducto'],'A',request.form['producto'])
    odao = OfertasDAO()
    odao.insertarOferta(o)
    return redirect(url_for('ofertas'))
@app.route('/consultarOferta/<id>/<idP>')
def consultarOferta(id,idP):
    odao = OfertasDAO()
    o=odao.consultaIndividual(id)
    conx = Conexion()
    db = conx.getDB()
    lista = []
    sql = 'select idProducto,nombre from Compras.Productos'
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    for dato in data:
        fila = {"id": str(dato[0]), "nombre": dato[1]}
        lista.append(fila)
    cursor.close()
    db.close()
    return render_template('Ventas/Editar/editarOferta.html',oferta=o,productos=lista,idP=idP,user=session.get('user'))
@app.route('/editarOferta',methods=['POST'])
def editarOferta():
    o = Oferta(request.form['id'],request.form['nombre'],request.form['descripcion'],request.form['descuento'],
                request.form['fechaInicio'],request.form['fechaFin'],request.form['canMinProducto'],'A',request.form['producto'])
    odao = OfertasDAO()
    odao.actualizar(o)
    return redirect(url_for('ofertas'))
@app.route('/eliminarOferta/<id>')
def eliminarOferta(id):
    odao = OfertasDAO()
    odao.eliminar(id)
    return redirect(url_for('ofertas'))
@app.route('/ofertasAsociacion')
def ofertasAsociacion():
    oadao = OfertasAsociacionDAO()
    lista = oadao.obtenerOfertasAsociacion()
    return render_template('Ventas/OfertasAsociacion.html', aos=lista, user=session.get('user'))
@app.route('/nuevaOfertaAsociacion')
def nuevoOfertaAsociacion():
    mdao = MiembrosDAO()
    conx = Conexion()
    db = conx.getDB()
    lista1 = []
    lista2 = []
    sql = "select idAsociacion,nombre from Ventas.Asociaciones where estatus='A'"
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    for dato in data:
        fila = {"id": dato[0], "nombre": dato[1]}
        lista1.append(fila)
    sql = "select idOferta,nombre from Ventas.Ofertas where estatus='A'"
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    for dato in data:
        fila = {"id": dato[0], "nombre": dato[1]}
        lista2.append(fila)
    cursor.close()
    db.close()
    return render_template('Ventas/Insertar/agregarOfertaAsociacion.html',asociaciones=lista1,ofertas=lista2,user=session.get('user'))
@app.route('/agregarOfertaAsociacion',methods=['POST'])
def agregarOfertaAsociacion():
    oa = OfertaAsociacion(request.form['asociacion'],request.form['oferta'],'A')
    oadao = OfertasAsociacionDAO()
    oadao.insertarOfertaAsociacion(oa)
    return redirect(url_for('ofertasAsociacion'))
@app.route('/consultarOfertaAsociacion/<idA>/<idO>')
def consultarOfertaAsociacion(idA,idO):
    oadao = OfertasAsociacionDAO()
    oa=oadao.consultaIndividual(idA,idO)
    conx = Conexion()
    db = conx.getDB()
    lista1 = []
    lista2 = []
    sql = "select idAsociacion,nombre from Ventas.Asociaciones where estatus='A'"
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    for dato in data:
        fila = {"id": str(dato[0]), "nombre": dato[1]}
        lista1.append(fila)
    sql = "select idOferta,nombre from Ventas.Ofertas where estatus='A'"
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    for dato in data:
        fila = {"id": str(dato[0]), "nombre": dato[1]}
        lista2.append(fila)
    cursor.close()
    db.close()
    return render_template('Ventas/Editar/editarOfertaAsociacion.html',oa=oa,asociaciones=lista1,idA=idA,idO=idO,ofertas=lista2,user=session.get('user'))
@app.route('/editarOfertaAsociacion/<idA>/<idO>',methods=['POST'])
def actualizarOfertaAsociacion(idA,idO):
    oa = OfertaAsociacion(request.form['asociacion'],request.form['oferta'],'A')
    oadao = OfertasAsociacionDAO()
    oadao.actualizar(oa,idA,idO)
    return redirect(url_for('ofertasAsociacion'))
@app.route('/eliminarOfertaAsociacion/<idA>/<idO>')
def eliminarOfertaAsociacion(idA,idO):
    oadao = OfertasAsociacionDAO()
    oadao.eliminar(idA,idO)
    return redirect(url_for('ofertasAsociacion'))
>>>>>>> Stashed changes

if __name__=='__main__':
    app.run(debug=True)
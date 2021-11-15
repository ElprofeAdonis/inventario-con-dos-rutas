from enum import unique
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root@localhost/sistema_de_inventario"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
api = Api(app)

#Desarrollar una API de un sistema de inventario
class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    codigoDeIdentificacion = db.Column(db.String(80), nullable=False)
    precio = db.Column(db.String(120), nullable=True)
    categoria = db.Column(db.String(100), nullable=False)
    fotografia = db.Column(db.String(2000), nullable=False)
    descripcion = db.Column(db.String(2000), nullable=False)
    anotacionDeGerente = db.Column(db.String(2000), nullable=False)

    def __repr__(self):
        return "<Elemento %r>" % self.username

#control de empleados
class Colaborador(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    codigoDeIdentificacion = db.Column(db.String(80), nullable=False)
    puesto = db.Column(db.String(120), nullable=True)
    rol = db.Column(db.String(100), nullable=False)
    fotografia = db.Column(db.String(2000), nullable=False)
    descripcion = db.Column(db.String(2000), nullable=False)
    anotacionDeGerente = db.Column(db.String(2000), nullable=False)

    def __repr__(self):
        return "<Funcionario %r>" % self.username



# *Controllers
class IndexRoute(Resource):
    def get(self):
        return {"response": "Hola, este es el index route :)"}

#control de empleados
class IndexRoute1(Resource):
    def get(self):
        return {"response": "Hola, este es el index route :)"}


class IndexElemento(Resource):
    def get(self):
        item = User.query.all()
        response = []
        if item:
            for elemento in item:
                response.append(
                    {
                        "id": elemento.id,
                        "username": elemento.username,
                        "codigoDeIdentificacion": elemento.codigoDeIdentificacion,
                        "precio": elemento.precio,
                        "categoria": elemento.categoria,
                        "fotografia": elemento.fotografia,
                        "descripcion": elemento.descripcion,
                        "anotacionDeGerente": elemento.anotacionDeGerente,
                    }
                )

        return {"response": response}, 200

    def post(self):
        elementoACrear = request.get_json()
        if (elementoACrear['username'] == "" or elementoACrear['codigoDeIdentificacion'] == "" or elementoACrear['precio'] == ""):
            return { "response": "Error al ingregar los datos, revise que todos los campos requeridos tengan informacion mmmmm"}, 400
        elemento = User(username=elementoACrear['username'], codigoDeIdentificacion=elementoACrear['codigoDeIdentificacion'], precio=elementoACrear['precio'], categoria=elementoACrear['categoria'], fotografia=elementoACrear['fotografia'], descripcion=elementoACrear['descripcion'], anotacionDeGerente=elementoACrear['anotacionDeGerente'])
        db.session.add(elemento)
        db.session.commit()
        return { "response": " item creado exitosamente!"}, 201

#index de empleado
class Funcionario(Resource):
    def get(self):
        empleado = Colaborador.query.all()
        response = []
        if empleado:
            for funcionario in empleado:
                response.append(
                    {
                        "id": funcionario.id,
                        "username": funcionario.username,
                        "codigoDeIdentificacion": funcionario.codigoDeIdentificacion,
                        "puesto": funcionario.puesto,
                        "rol": funcionario.rol,
                        "fotografia": funcionario.fotografia,
                        "descripcion": funcionario.descripcion,
                        "anotacionDeGerente": funcionario.anotacionDeGerente,
                    }
                )

        return {"response": response}, 200

    def post(self):
        funcionarioACrear = request.get_json()
        if (funcionarioACrear['username'] == "" or funcionarioACrear['codigoDeIdentificacion'] == "" or funcionarioACrear['puesto'] == "" or funcionarioACrear['rol'] == ""):
            return { "response": "Error al ingregar los datos, revise que todos los campos requeridos tengan informacion hola"}, 400
        funcionario = Colaborador(username=funcionarioACrear['username'], codigoDeIdentificacion=funcionarioACrear['codigoDeIdentificacion'], puesto=funcionarioACrear['puesto'], rol=funcionarioACrear['rol'], fotografia=funcionarioACrear['fotografia'], descripcion=funcionarioACrear['descripcion'], anotacionDeGerente=funcionarioACrear['anotacionDeGerente'])
        db.session.add(funcionario)
        db.session.commit()
        return { "response": " empleado creado exitosamente!"}, 201


class UserById(Resource):
    def get(self, id):
        elemento = User.query.filter_by(id=id).first()

        if (elemento is None):
            return { "response": "Error al obtener los datos, el empleado no existe."}, 400
 
        return {'response': {
            "id": elemento.id,
            "username": elemento.username,
            "codigoDeIdentificacion": elemento.codigoDeIdentificacion,
            "precio": elemento.precio,
            "categoria": elemento.categoria,
            "fotografia" : elemento.fotografia,
            "descripcion": elemento.descripcion,
            "anotacionDeGerente": elemento.anotacionDeGerente
        }}, 200

    def put(self, id):
        elemento = User.query.filter_by(id=id).first()
        datos = request.get_json()
        # TODO: LOOKUP 'ARGUMENT PARSING for Flask-RESTful'
        if (datos['username'] == "" or datos['username'] is None or datos['codigoDeIdentificacion'] == "" or datos['codigoDeIdentificacion'] is None or datos['precio'] == "" or datos['precio'] is None):
            return { "response": "Error al actualizar los datos, empleado no existe."}, 400

        elemento.username = datos['username']
        elemento.codigoDeIdentificacion = datos['codigoDeIdentificacion']
        elemento.puesto = datos['puesto']
        elemento.rol = datos['rol']
        elemento.fotografia = datos['fotografia']
        elemento.descripcion = datos['descripcion']
        elemento.anotacionDeGerente = datos['anotacionDeGerente']
        db.session.commit()
 
        return {"response": "elemento actualizado con exito!"}

    def delete(self, id):
        elemento = User.query.filter_by(id=id).first()

        if (elemento is None):
            return { "response": "Error al borrar los datos, el item no existe."}, 400

        db.session.delete(elemento)
        db.session.commit()
        return { "response": "elemento con id: {anime}. Borrado exitosamente. ".format(elemento=id)}, 203


# Byid de emplado
class ColaboradorById(Resource):
    def get(self, id):
        funcionario = Colaborador.query.filter_by(id=id).first()

        if (funcionario is None):
            return { "response": "Error al obtener los datos, el elemento no existe."}, 400
 
        return {'response': {
            "id": funcionario.id,
            "username": funcionario.username,
            "codigoDeIdentificacion": funcionario.codigoDeIdentificacion,
            "puesto": funcionario.puesto,
            "rol": funcionario.rol,
            "fotografia" : funcionario.fotografia,
            "descripcion": funcionario.descripcion,
            "anotacionDeGerente": funcionario.anotacionDeGerente
        }}, 200

    def put(self, id):
        funcionario = Colaborador.query.filter_by(id=id).first()
        datos = request.get_json()
        # TODO: LOOKUP 'ARGUMENT PARSING for Flask-RESTful'
        if (datos['username'] == "" or datos['username'] is None or datos['codigoDeIdentificacion'] == "" or datos['codigoDeIdentificacion'] is None or datos['puesto'] == "" or datos['puesto'] is None or datos['rol'] == "" or datos['rol'] is None):
            return { "response": "Error al actualizar los datos, item no existe."}, 400

        funcionario.username = datos['username']
        funcionario.codigoDeIdentificacion = datos['codigoDeIdentificacion']
        funcionario.puesto = datos['puesto']
        funcionario.rol = datos['rol']
        funcionario.fotografia = datos['fotografia']
        funcionario.descripcion = datos['descripcion']
        funcionario.anotacionDeGerente = datos['anotacionDeGerente']
        db.session.commit()
 
        return {"response": "elemento actualizado con exito!"}

    def delete(self, id):
        funcionario = Colaborador.query.filter_by(id=id).first()

        if (funcionario is None):
            return { "response": "Error al borrar los datos, el empleado no existe."}, 400

        db.session.delete(funcionario)
        db.session.commit()
        return { "response": "elemento con id: {funcionario}. Borrado exitosamente. ".format(funcionario=id)}, 203

db.create_all()

# *Routes
# GET
api.add_resource(IndexRoute, '/')
api.add_resource(IndexRoute1, '/')
# GET, POST
api.add_resource(IndexElemento, '/item')
api.add_resource(Funcionario, '/empleado')
# GET, PUT, DELETE
api.add_resource(UserById, '/item/<int:id>')
api.add_resource(ColaboradorById, '/empleado/<int:id>')
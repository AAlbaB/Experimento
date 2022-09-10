from datetime import datetime
from flaskr import create_app
from flask import request
from flask_restful import Api, Resource
from .modelos import db, Usuario, UsuarioSchema
from celery import Celery

celery_app = Celery('tasks', broker = 'redis://localhost:6379/0')

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()
usuario_schema = UsuarioSchema()

@celery_app.task(name='login.log')
def registrar_log(usuario, fecha):
    pass

class VistaLogin(Resource):
    def post(self):
        usuario = Usuario.query.filter(Usuario.usuario == request.json["usuario"],
                                       Usuario.contrasena == request.json["contrasena"]).first()
        db.session.commit()
        if usuario is None:
            return "El usuario no existe", 401
        else:
            args = (request.json["usuario"], datetime.utcnow())
            registrar_log.apply_async(args=args)
            return {"mensaje": "Inicio de sesión exitoso"}, 200

api = Api(app)
api.add_resource(VistaLogin, '/login')
import base64
from flask import request
from ..modelos import db, Usuario, UsuarioSchema
from flask_restful import Resource
from datetime import datetime
from celery import Celery

celery_app = Celery(__name__, broker='redis://localhost:6379/0')

usuario_schema = UsuarioSchema()

@celery_app.task(name='registrar_log')
def registrar_log(*args):
    pass

class VistaSignIn(Resource):

    def post(self):
        contra = request.json["contrasena"].encode("utf-8")
        contra_encode = base64.b64encode(contra)

        tarjeta = request.json["tarjeta"].encode("utf-8")
        tarjeta_encode = base64.b64encode(tarjeta)
        
        nuevo_usuario = Usuario(usuario=request.json["usuario"],
                                contrasena=contra_encode,
                                tarjeta=tarjeta_encode)
        db.session.add(nuevo_usuario)
        db.session.commit()
        return {"mensaje": "Usuario creado exitosamente", "id": nuevo_usuario.id}


class VistaLogIn(Resource):

    def post(self):
        usuario = Usuario.query.filter(Usuario.usuario == request.json["usuario"],
                                       Usuario.contrasena == request.json["contrasena"]).first()
        db.session.commit()
        if usuario is None:
            return "El usuario no existe", 401
        else:
            args = (request.json["usuario"], datetime.utcnow())
            registrar_log.apply_async(args=args, queue='logs')
            return {"mensaje": "Inicio de sesión exitoso"}, 200

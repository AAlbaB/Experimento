from flask import request
from ..modelos import db, Usuario, UsuarioSchema
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

usuario_schema = UsuarioSchema()


class VistaSignIn(Resource):

    def post(self):
        nuevo_usuario = Usuario(usuario=request.json["usuario"],
                                contrasena=request.json["contrasena"],
                                tarjeta=request.json["tarjeta"])
        db.session.add(nuevo_usuario)
        db.session.commit()
        return {"mensaje": "Usuario creado exitosamente", "id": nuevo_usuario.id}


class VistaLogIn(Resource):

    def post(self):
        usuario = Usuario.query.filter(Usuario.usuario == request.json["usuario"],
                                       Usuario.contrasena == request.json["contrasena"]).first()
        db.session.commit()
        if usuario is None:
            return "El usuario no existe", 404
        else:
            return {"mensaje": "Inicio de sesión exitoso"}

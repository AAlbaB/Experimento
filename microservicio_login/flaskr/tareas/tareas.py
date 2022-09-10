from ..app import db
from ..modelos import Usuario, UsuarioSchema
import os
from celery import Celery
from celery.signals import task_postrun

celery_app = Celery('tasks', broker = 'redis://localhost:6379/0')

usuario_schema = UsuarioSchema()

@celery_app.task(name='login.log')
def registrar_log(usuario, fecha):
    with open('log_login.txt', 'a+') as file:
        file.write('{} - Inicio de sesion: {}\n'.format(usuario, fecha))
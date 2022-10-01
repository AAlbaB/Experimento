### Objetivo:
La finalidad de este experimento es probar la arquitectura propuesta para favorecer la disponibilidad de un servicio de login.

### Pasos para ejecutar:
1. Se debe instalar el entorno virtual, con windows: ```python -m venv venv``` y con Linux: ```python3 -m venv venv```
2. Activar el entorno virtual, con windows: ```.\venv\Scripts\activate``` y con Linux: ```source venv/bin/activate```
3. Instalar los requirements: ```python -m pip install -r requirements.txt```
4. Para ejecutar, en la raiz del proyecto ejecutar: ```redis-server```
5. Ejecutamos la aplicación monolitica: ```cd flaskr y flask run -p 5000```
6. Ejecutamos el microservicio: ```cd microservicio_login```, ```cd flaskr``` y ```flask run -p 5001```
7. Desde Postman hacer un login con el usuario y contraseña conrrecto a: ```localhost:5001/login```
8. Si los datos ingresados son correctos, se debería generar un token de autorización para poder visualizar los datos de la persona
9. Hamos la petición al microservicio para visualizar los datos: ```localhost:5001/reglas/{id_usuario}```
10. No olvidar en el paso anterior ingresar el token de autorización, en caso contrario no se retorna los datos solicitados.
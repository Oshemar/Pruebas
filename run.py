#Importar
from flask import Flask

#Crear app medante instancia
app = Flask(__name__)

#Crear rutas con sus correspondientes funciones
@app.route('/')
def holamundo():
    return 'Hola Mundo!'

@app.route('/Pruebas')
def mostrarproyectos():
    return 'Aqie se muestran mis proyectos'
#Ejecutar nuestra app cuando ejecutemos este archivo run.py

if __name__ == '__main__':
    app.run(debug=True)
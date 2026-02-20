import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

#Cargar las variables de entorno
load_dotenv()

#crear instancia
app =  Flask(__name__)

# Configuración de la base de datos PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#Modelo de la base de datos
class Mercancia(db.Model):
    __tablename__ = 'mercancias'
    id_mercancia = db.Column(db.String, primary_key=True)
    nombre = db.Column(db.String)
    color = db.Column(db.String)
    precio = db.Column(db.Integer)

    def to_dict(self):
        return{
            'id_mercancia': self.id_mercancia,
            'nombre': self.nombre,
            'color': self.color,
            'precio': self.precio,
        }


#Ruta raiz
@app.route('/')
def index():
    #Trae todos los estudiantes
    mercancias = Mercancia.query.all()
    #return estudiantes
    return render_template('index.html', mercancias = mercancias)
"""

#Ruta /alumnos crear un nuevo alumno
@app.route('/estudiantes/new', methods=['GET','POST'])
def create_estudiante():
    if request.method == 'POST':
        #Agregar Estudiante
        no_control = request.form['no_control']
        nombre = request.form['nombre']
        ap_paterno = request.form['ap_paterno']
        ap_materno = request.form['ap_materno']
        semestre = request.form['semestre']

        nvo_estudiante = Estudiante(no_control=no_control, nombre=nombre, ap_paterno=ap_paterno, ap_materno= ap_materno, semestre= semestre)

        db.session.add(nvo_estudiante)
        db.session.commit()

        return redirect(url_for('index'))
    
    #Aqui sigue si es GET
    return render_template('create_estudiante.html')

#Actualizar estudiante
@app.route('/estudiantes/update/<string:no_control>', methods=['GET','POST'])
def update_estudiante(no_control):
    estudiante = Estudiante.query.get(no_control)
    if request.method == 'POST':
        estudiante.nombre = request.form['nombre']
        estudiante.ap_paterno = request.form['ap_paterno']
        estudiante.ap_materno = request.form['ap_materno']
        estudiante.semestre = request.form['semestre']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update_estudiante.html', estudiante=estudiante)

#Eliminar estudiante
@app.route('/estudiantes/delete/<string:no_control>')
def delete_estudiante(no_control):
    estudiante = Estudiante.query.get(no_control)
    if estudiante:
        db.session.delete(estudiante)
        db.session.commit()
    return redirect(url_for('index'))
"""

if __name__ == '__main__':
    app.run(debug=True)
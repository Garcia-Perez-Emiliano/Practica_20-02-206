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
    #Trae todas las mercacias
    mercancias = Mercancia.query.all()
    #return mercacias
    return render_template('index.html', mercancias = mercancias)


#Ruta crear nueva mercacia
@app.route('/new', methods=['GET','POST'])
def create_mercancia():
    if request.method == 'POST':
        #Agregar Mercancias
        id_mercancia = request.form['id_mercancia']
        nombre = request.form['nombre']
        color = request.form['color']
        precio = request.form['precio']

        nvo_mercancia = Mercancia(id_mercancia=id_mercancia, nombre=nombre, color=color, precio= precio)

        db.session.add(nvo_mercancia)
        db.session.commit()

        return redirect(url_for('index'))
    
    #Aqui sigue si es GET
    return render_template('create_mercancia.html')


#Actualizar mercancia
@app.route('/update/<string:id_mercancia>', methods=['GET','POST'])
def update_mercancia(id_mercancia):
    mercancia = Mercancia.query.get(id_mercancia)
    if request.method == 'POST':
        mercancia.nombre = request.form['nombre']
        mercancia.color = request.form['color']
        mercancia.precio = request.form['precio']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update_mercancia.html', mercancia=mercancia)

#Eliminar mercancia
@app.route('/delete/<string:id_mercancia>')
def delete_mercancia(id_mercancia):
    mercancia = Mercancia.query.get(id_mercancia)
    if mercancia:
        db.session.delete(mercancia)
        db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
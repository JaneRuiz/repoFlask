from flask import Blueprint, render_template, session, redirect, url_for, flash
from ..models import Usuario, Vacante     # los dos puntos es para subir el directorio arriba

main_bp = Blueprint('main', __name__)        #ordenar la rutas asignandole un nombre main 

@main_bp.route('/')  #se pone el arroba como un decorador de una funcion y especicifar la ruta exacta
def index():         # Se define la funcion
    vacantes = Vacante.query.order_by(Vacante.fecha_publicacion.desc()).limit(3).all()

    return render_template('index.html', vacantes=vacantes)  #se envia a la vista

@main_bp.route('/acerca')
def acerca():
    return render_template('acerca.html')

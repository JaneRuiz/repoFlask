from flask import Flask
from .models import db, Usuario
import os
from .routes.main_routes import main_bp
from .routes.vacante_routes import vacante_bp

def create_app():    #es la funcion que sirve para inicializar y crear la app
    app = Flask(__name__)
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, '..','base_vacantes.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)   #inicializa la base de datos, crea el archivo y los campos

    with app.app_context():             #Accese a la instqvcia ya la variable 
        db.create_all()                   #Crea las tablas y las actualiza
        if not Usuario.query.filter_by(username='admin').first():   #Crear u usuariuo por defecto pero hace una comparacion 
            admin = Usuario (                     #Se llama admin el usuario
                username= 'admin',
                email= 'admin@mycompany.com',
                password= 'admin123',
                estatus= 'Activo'
            )
            db.session.add(admin)     #Insertar el usuario en la tabla y lo reconcoe automaticametne 
            db.session.commit()
    
    app.register_blueprint(main_bp)
    app.register_blueprint(vacante_bp)

    return app                        #REtorna la instancia 






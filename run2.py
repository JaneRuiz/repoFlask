 #Este archivo lo que haces es direccionar una pagina web en blanco
from flask import Flask     #importa la libreria flask
app = Flask(__name__)   #crea una instancia de la aplicacion para manipular la instancia es app'''
@app.route ('/')       
def hello():              #define la funcion hello
    return "Hola, bienvenidos al curso de Framewoks Flask "
if __name__== '__main__':    # definimos la funcion principal desde aqui inicia la ejecucuin del programa, marcamos el inicio
    app.run(debug=True)    #iniciar el servidor y cada cambio que se haga en el Retur solo de guarda y se recarga la pagina



    

from unittest import result
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template("formulario.html")


@app.route('/procesar', methods=['POST'])
def procesar():
    resul = request.form['texto_hilo']
    
   
    try:
        resultado=(eval(resul))
    except:
        print('')



    return render_template("formulario.html", resultado=resultado)



if __name__ == "__main__":
    app.run(port=3000, debug=True)


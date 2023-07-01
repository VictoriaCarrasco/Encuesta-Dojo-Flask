from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/formulario', methods=['POST'])
def formulario():
    print("Got post Info")
    print (request.form)
    return redirect ('/results')


@app.route('/results', methods=['POST'])
def results():
    if request.method == 'POST':
        name = request.form['name']
        pais = request.form['pais']
        lenguaje = request.form['lenguaje']
        comentario = request.form['comentario']
        print(name)
        print(pais)
        print(lenguaje)
        return render_template('results.html', name=name, pais=pais, lenguaje=lenguaje, comentario=comentario)
    else:
        return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
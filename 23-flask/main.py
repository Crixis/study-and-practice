from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/informacion')
def informacion():
    return render_template('informacion.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/lenguajes-de-programacion')
def lenguajes():
    return render_template('lenguajes.html')


if __name__== '__main__':
    app.run(debug=True)
from django.shortcuts import render, HttpResponse

# Create your views here.
#MVC = modelo vista controlador -> Acciones(metodos)
#MVT = modelo vista template -> Acciones(metodos)

def index(request):
    nombre='Cristian Vargas'
    lenguajes=['javascript','python','php','c']
    return render(request, "index.html", {
        'mi_variable':'soy un dato que esta en la vista',
        'nombre':nombre,
        'lenguajes':lenguajes
    })

def hola_mundo(request):
    return render(request, "holamundo.html")

def pagina(request):
    return render(request, "pagina.html")


from django.http import HttpResponse

# Esta es nuestra primera "vista", es una función python y recibe un objeto
# de tipo HttpResponse como argumento (request), recordar añadir esta vista
# a su url respectivo.
def saludo(request):
    # Retorna un objeto de tipo HttpResponse que muestra el contenido del 
    # string en su argumento
    '''return HttpResponse("Hola alumnos esta es nuestra primera página con \
        Django")'''
    
    # El parámetro de HttpResponse recibe argumentos con código HTML en forma
    # de strings
    '''return HttpResponse("<html><body><h1>Hola alumnos esta es nuestra \
        primera página con Django</html></body></h1>")'''
    
    # Es preferible definir una variable que contenga todo el código HTML y
    # pasar esta variable como argumento del HttpResponse, para definir
    # una cadena de texto con varias líneas se utilizan las triples comillas.
    documento = """
    <html>
        <body>
            <h1>Hola alumnos esta es nuestra primera página con Django</h1>
        </body>
    </html>
    """
    return HttpResponse(documento)

# Esta es otra "vista" que de igual forma debe registrarse en "urls.py".
def despedida(request):
    return HttpResponse("Hasta luego alumnos de Django")

# Esta es una vista con contenido dinámico
def dame
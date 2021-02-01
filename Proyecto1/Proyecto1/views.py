from django.http import HttpResponse

# Esta es nuestra primera "vista", es una función python y recibe un objeto
# de tipo HttpResponse como argumento (request), recordar añadir esta vista
# a su url respectivo.

def saludo(request):
    # Retorna un objeto de tipo HttpResponse
    return HttpResponse("Hola alumnos esta es nuestra primera página con \
                        Django")
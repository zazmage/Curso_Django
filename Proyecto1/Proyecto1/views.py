from django.http import HttpResponse
import datetime
# Se importa la clase "Template" y "Context" desde el módulo "django.template"
from django.template import Template, Context

# Definiendo nuestras propias clases para hacer uso de sus objetos dentro de 
# nuestras plantillas.
class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

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
    
    # La cadena de texto al interior de la variable documento contiene código
    # HTML sin embargo esto se considera una mala práctica de programación
    # en este caso se hará uso de plantillas para organizar mejor el proyecto.
    '''
    documento = """
    <html>
        <body>
            <h1>Hola alumnos esta es nuestra primera página con Django</h1>
        </body>
    </html>
    """
    '''
    # Inicializando un objeto de la clase Persona creada anteriormente para 
    # pasarlo como parámetro al contexto.
    p1 = Persona("Profesor Manuel", "Díaz")
    # Prueba condicionales con operadores de comparación en la plantilla.
    '''
    p1 = Persona("Profesor Manuel", "Díaz")
    '''
    
    # Se puede inicializar una variable para pasarla como parámetro al objeto
    # del contexto o se puede pasar directamente el valor de la variable como
    # parámetro.
    '''
    nombre = "Juan"
    apellido = "Díaz"
    '''
    # Definiendo la lista para pasar como parámetro al contexto.
    temasDelCurso = ["Plantillas","Modelos","Formularios","Vistas",
                     "Despliegue"]
    
    # Caso lista vacía
    '''
    temasDelCurso = []
    '''
    
    ahora = datetime.datetime.now()
    
    # Se recomienda separar la dirección con slash (/)
    doc_externo = open("Proyecto1/plantillas/miplantilla.html")
    
    # Se debe importar la clase Template
    # Se crea un objeto de tipo "Template" al que se le cargará el código HTML
    # del archivo "miplantilla.html"
    plt = Template(doc_externo.read())
    
    doc_externo.close()
    
    # Se debe importar la clase Context
    # Se crea un objeto de tipo "Context" que de momento estará vacío debido
    # a que de momento no tiene contenido dinámico.
    '''
    ctx = Context({})
    '''
    
    # El contexto recibe como argumento un diccionario en el cual podemos
    # especificar el contenido en forma de variables u objetos que queremos
    # implementar en nuestras vista, si se desean añadir más variables,
    # simplemente se agregan más elementos al diccionario.
    '''
    ctx = Context({
        "nombre_persona": nombre, 
        "apellido_persona": apellido,
        "momento_actual":ahora
        })
    '''

    # Pasando directamente un parámetro al context
    '''
    ctx = Context({"nombre_persona": "Juan", "apellido_persona": "Díaz"})
    '''
    
    # Pasando como parámetro un objeto de la clase Persona, creada 
    # anteriomente y una lista de python.
    ctx = Context({
        "nombre_persona": p1.nombre, 
        "apellido_persona": p1.apellido,
        "momento_actual":ahora,
        "temas": temasDelCurso
        })
    
    # La función "render" del objeto plt sirve para "renderizar" la vista en
    # la página, se le pasa el objeto ctx de tipo "Context" creado 
    # anteriormente.
    documento = plt.render(ctx)
    
    return HttpResponse(documento)

# Esta es otra "vista" que de igual forma debe registrarse en "urls.py".
def despedida(request):
    return HttpResponse("Hasta luego alumnos de Django")

# Esta es una vista con contenido dinámico
def dameFecha(request):
    # Para usar el modulo "datetime" es necesario importarlo
    fecha_actual = datetime.datetime.now()
    
    # %s es un marcador de posición
    # % indica la variable que va en ese marcador de posición
    documento = """
    <html>
        <body>
            <h2>Fecha y hora actuales %s</h2>
        </body>
    </html>
    """ %fecha_actual
    
    return HttpResponse(documento)

# Esta vista / función calculará una edad según el parámetro que se pase
# desde la url
def calculaEdad(request, edad, agno):
    
    periodo = agno - 2021
    edadFutura = edad + periodo
    documento = """
    <html>
        <body>
            <h2>En el año %s tendrás %s años</h2>
        </body>
    </html>
    """ %(agno,edadFutura)
    
    return HttpResponse(documento)
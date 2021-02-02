"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# Importa el módulo views con las vistas correspondientes
# from Proyecto1.views import saludo
# De igual forma importa la vista "despedida" del módulo views.py
# from Proyecto1.views import despedida
# Tambíen se puede usar from Proyecto1.views import saludo, despedida

from Proyecto1.views import saludo, despedida, dameFecha, calculaEdad


# Aquí se añaden las url de nuestra página.
urlpatterns = [
    path('admin/', admin.site.urls),
    # Url de la vista saludo definido en otro módulo de python por lo que
    # debe importarse dicho módulo para que se pueda reconocer la función.
    path('saludo/', saludo),
    path('nosveremos/', despedida),
    path('fecha/', dameFecha),
    # El paso de parámetros por url se especifica en corchetes angulares (<>)
    # "int:" Convierte el parámetro agno de string a entero.
    # Para pasar más de un parámetro simplemente se especifíca el parámetro
    # entre corchetes angulares y se separan los parametros con un slash.
    path('edades/<int:edad>/<int:agno>', calculaEdad),
]

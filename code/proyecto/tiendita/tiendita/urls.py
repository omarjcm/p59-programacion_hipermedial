"""tiendita URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from tiendita import views as locals_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', locals_views.hello_world),
    path('hola/', locals_views.hola),
    path('obtener-numeros/', locals_views.obtener_numeros),
    path('obtener-numeros-ordenados/', locals_views.obtener_numeros_ordenados),
    path('persona/', locals_views.persona),
    path('persona2/', locals_views.persona2)
]

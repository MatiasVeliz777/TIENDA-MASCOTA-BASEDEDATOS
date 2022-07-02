from unicodedata import name
from django.urls import  path
from .views import  *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('',index,name="index"),
    path('catalogo-prod',catalogoprod,name="catalogo-prod"),
    path('Crud-prod',Crudprod,name="Crud-prod"),
    path('eliminarProd/<int:id>', eliminarProd, name="eliminarProd"),
    path('eliminarPromo/<int:id>', eliminarPromo, name="eliminarPromo"),
    path('editarProd/<int:id>', editarProd, name="editarProd"),
    path('editarPromo/<int:id>', editarPromo, name="editarPromo"),
    path('crearProd',crearProd,name="crearProd"),
    path('crearPromo',crearPromo,name="crearPromo"),
    path('Crud-prom',Crudprom,name="Crud-prom"),
    path('plantilla',plantilla,name="plantilla"),
    path('subscripciones',subscripciones,name="subscripciones"),
    path('Ver-compras',Vercompras,name="Ver-compras"),
    path('login', LoginView.as_view(template_name="core/login.html"), name="login"),
    path('logout', LogoutView.as_view(template_name="core/logout.html"), name="logout"),
    path('registro', registro, name="registro"),
    


]
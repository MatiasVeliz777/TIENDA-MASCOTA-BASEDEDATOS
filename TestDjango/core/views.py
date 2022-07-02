from django.shortcuts import render, redirect
from .models import * 
from .forms import *
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def index(request):
    prod = Producto.objects.all()
    return render(request, 'core/index.html',{'prod' : prod})


def catalogoprod(request):
    prod = Producto.objects.all()  
    print(prod)
    return render(request, 'core/catalogo-prod.html', {'prod' : prod})

def Crudprod(request):
    prod = Producto.objects.all()     
    return render(request, 'core/Crud-prod.html', {'prod' : prod})

def crearProd(request):
    formulario = ProductoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('Crud-prod')
    return render(request, 'core/crearProd.html', {'formulario': formulario})

def crearPromo(request):
    formulario = PromocionForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('Crud-prom')
    return render(request, 'core/crearPromo.html', {'formulario': formulario})

def Crudprom(request):
    prom = Promocion.objects.all()     
    return render(request, 'core/Crud-prom.html', {'prom' : prom})

def eliminarProd(request, id):
    prod = Producto.objects.get(idProducto = id)
    prod.delete()
    return redirect('Crud-prod')

def eliminarPromo(request, id):
    prom = Promocion.objects.get(idPromocion = id)
    prom.delete()
    return redirect('Crud-prom')

def editarProd(request, id):
    prod = Producto.objects.get(idProducto = id)
    formulario = ProductoForm(request.POST or None, request.FILES or None, instance=prod)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('Crud-prod')
    return render(request, 'core/editarProd.html', {'formulario': formulario})

def editarPromo(request, id):
    promo = Promocion.objects.get(idPromocion = id)
    formulario = PromocionForm(request.POST or None, request.FILES or None, instance=promo)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('Crud-prom')
    return render(request, 'core/editarPromo.html', {'formulario': formulario})


def plantilla(request):
    
    return render(request, 'core/plantilla.html') 

def subscripciones(request):
    
    return render(request, 'core/subscripciones.html')    

def Vercompras(request):
    
    return render(request, 'core/Ver-compras.html') 

def listarProductos(request):
    prod = Producto.objects.all()  
    print(prod)
    return render(request, 'core/Crud-prod.html', {'prod' : prod})

def registro(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="login")
    return render(request, 'core/registro.html', {'form':form})


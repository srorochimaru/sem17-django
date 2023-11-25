from django.shortcuts import render
from .models import Cliente,Empleado,Factura,Registro
# Create your views here.
def Lista1(request):
    listaso1 = Cliente.objects.all()
    # Cambiar el nombre del diccionario a "clientes"
    return render(request,"Cliente.html", {"clientes":listaso1})

def Lista2(request):
    listado2 = Empleado.objects.all()
    return render(request,"Empleado.html", {"empleado":listado2})

def Lista3(request):
    Listado3 = Factura.objects.all()
    return render(request,"Facturas.html", {"factura": Listado3})

def lista4(request):
    listado4 = Registro.objects.all()
    return render(request,"Registros.html", {"registro":listado4})
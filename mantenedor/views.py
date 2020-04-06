from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib import messages


from .models import Equivalente, Rodamiento, Tipo_Rodamiento
from .forms import tipoForm, rodForm, equivForm
from .filters import RodamientoFilter, EquivFilter, TipoFilter
# Create your views here.

# --- Tipo_Rodamiento CRUD:
def listar_tipo(request):
    lista_tipo = Tipo_Rodamiento.objects.all()
    lista_tipo_filter = TipoFilter(request.GET, queryset=lista_tipo)
    return render(request, 'tipo_rod/listar_tipo.html', {'filter' : lista_tipo_filter })


def agregar_tipo(request):
    if request.method == 'POST':
        form = tipoForm(request.POST)
        if form.is_valid():
            form.save()            
            TIPO = form.cleaned_data.get('TIPO')
            messages.success(request, f'Tipo Rodamiento: {TIPO} Agregado!')
            return redirect('/mantenedor/tipo_rod/agregar')
    else:
        form = tipoForm()
    return render(request, 'tipo_rod/agregar_tipo.html', {'form': form, 'titulo': 'Agregar Tipo Rodameinto'})


def editar_Tipo(request, tipo_id):
    instancia= Tipo_Rodamiento.objects.get(PK_TIPO_ROD=tipo_id)

    form=  tipoForm(instance=instancia)
    if request.method=="POST":
        form= tipoForm(request.POST, instance=instancia)
        if form.is_valid():
            instancia= form.save(commit=False)
            instancia.save()

            TIPO = form.cleaned_data.get('TIPO')
            messages.success(request, f'Tipo Rodamiento: {TIPO} Modificado!')

            return redirect('/mantenedor/tipo_rod/buscar')
    return render(request, "tipo_rod/editar_tipo.html",{'form': form, 'titulo': 'Modificar'}) 

def eliminar_tipo(request, tipo_id):
    instancia= Tipo_Rodamiento.objects.get(PK_TIPO_ROD=tipo_id)
    instancia.delete()
    messages.warning(request, f'Tipo Rodamiento {instancia.TIPO} Eliminado!')
    return redirect('/mantenedor/tipo_rod/buscar')

# --- Rodamiento CRUD:
def listar_rod(request):
    lista_rod = Rodamiento.objects.all()
    lista_equiv = Equivalente.objects.all()
    lista_rod_filter = RodamientoFilter(request.GET, queryset=lista_rod)
    return render(request, 'rodamiento/listar_rod.html', {'equiv': lista_equiv,'filter' : lista_rod_filter })

def agregar_rod(request):
    if request.method == 'POST':
        form = rodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()            
            messages.success(request, f'Rodamiento Agregado!')
            return redirect('/mantenedor/rod/agregar')
    else:
        form = rodForm()
    return render(request, 'rodamiento/agregar_rod.html', {'form': form, 'titulo': 'Agregar Tipo Rodameinto'})


def editar_rod(request, rod_id):
    instancia= Rodamiento.objects.get(PK_ROD=rod_id)
    form=  rodForm(instance=instancia)
    if request.method=="POST":
        form= rodForm(request.POST, request.FILES, instance=instancia)
        if form.is_valid():
            instancia= form.save(commit=False)
            instancia.save()
            messages.success(request, f'Rodamiento Modificado!')
            return redirect('/mantenedor/home')
    return render(request, "rodamiento/editar_rod.html",{'form': form, 'titulo': 'Modificar'}) 

def eliminar_rod(request, rod_id):
    instancia= Rodamiento.objects.get(PK_ROD=rod_id)
    instancia.delete()
    messages.warning(request, f'Rodamiento Eliminado!')
    return redirect('/mantenedor/home')

# --- Equivalente CRUD:
def listar_equiv(request):
    lista_equiv = Equivalente.objects.all()
    lista_equiv_filter = EquivFilter(request.GET, queryset=lista_equiv)
    return render(request, 'equivalente/listar_equiv.html', {'filter' : lista_equiv_filter })


def agregar_equiv(request,fk_rod):
    if request.method == 'POST':
        form = equivForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()            
            messages.success(request, f'Equivalente Agregado')
            return redirect('/mantenedor/home')
    else:
        form = equivForm()
    return render(request, 'equivalente/agregar_equiv.html', {'form': form, 'titulo': 'Agregar Tipo Rodameinto','fk_rod':fk_rod})


def editar_equiv(request, equiv_id):
    instancia= Equivalente.objects.get(id=equiv_id)

    form=  equivForm(instance=instancia)
    if request.method=="POST":
        form= equivForm(request.POST, request.FILES, instance=instancia)
        if form.is_valid():
            instancia= form.save(commit=False)
            instancia.save()
            messages.success(request, f'Equivalente Editado')
            return redirect('/mantenedor/equiva/buscar')
    return render(request, "equivalente/agregar_equiv.html",{'form': form, 'titulo': 'Modificar'}) 

def eliminar_equiv(request, equiv_id):
    instancia= Equivalente.objects.get(id=equiv_id)
    instancia.delete()
    messages.warning(request, f'Equivalente Eliminado')
    return redirect('/mantenedor/equiva/buscar')



#base
def home(request):
    return render(request, 'base/base.html')
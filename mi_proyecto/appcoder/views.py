# Create your views here.
from django.shortcuts import render, redirect
from .forms import ProfesorForm, AlumnoForm, EntregableForm

def inicio(request):
    return render(request, 'appcoder/inicio.html')

def agregar_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ProfesorForm()
    return render(request, 'appcoder/agregar_profesor.html', {'form': form})

def agregar_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = AlumnoForm()
    return render(request, 'appcoder/agregar_alumno.html', {'form': form})

def agregar_entregable(request):
    if request.method == 'POST':
        form = EntregableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = EntregableForm()
    return render(request, 'appcoder/agregar_entregable.html', {'form': form})

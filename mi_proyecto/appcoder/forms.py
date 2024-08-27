from django import forms
from .models import Profesor, Alumno, Entregable

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'

class EntregableForm(forms.ModelForm):
    class Meta:
        model = Entregable
        fields = '__all__'

from django.db import models

# Create your models here.
class Profesor(models.Model):
    Nombre = models.CharField(max_length=100)
    Materia = models.CharField(max_length=100)
    Email = models.EmailField()
    Especializacion = models.CharField(max_length=100)
    def __str__(self):
        return str(self.Nombre)


class Alumno(models.Model): 
    Id_del_Estudiante = models.CharField(max_length=100, unique=True) #Campo en el cual distingue al alumno como unico
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Edad = models.IntegerField()
    Nivel_Academico = models.CharField(max_length=50)
    Email = models.EmailField()
    def __str__(self):
        return f"{self.Nombre} {self.Apellido}"
    
class Curso(models.Model):
    Nombre = models.CharField(max_length=100)
    Descripcion = models.TextField()
    Duracion = models.IntegerField(help_text="Duración en horas o semanas")  
    Horarios = models.CharField(max_length=100)  
    Cupo_Maximo = models.IntegerField()  #maximo de estudiantes que se puede inscribir

    def __str__(self):
        return f"{self.Nombre} - {self.Duracion} horas"

class Entregable(models.Model):
    Nombre_Proyecto = models.CharField(max_length=100)
    Fecha_Entrega = models.DateField()
    Alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    Entregado = models.BooleanField(default=False)
    Calificacion = models.IntegerField(null=True, blank=True)  
    Comentario_Profesor = models.TextField(null=True, blank=True)  

    def __str__(self):
        return str(self.Nombre_Proyecto)

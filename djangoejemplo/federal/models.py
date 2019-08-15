from django.db import models

# Create your models here.


class Libro(models.Model):
    nombre=models.CharField(max_length=45)
    descripcion=models.CharField(max_length=45)
    isbn=models.CharField(max_length=45)
    copias=models.IntegerField(null=True)

    def __str__(self):
        return self.nombre

class Prestamo(models.Model):
    fechaprestamo=models.DateField("Fecha de Prestamo")
    nombrecliente=models.CharField(max_length=45)
    telefonocliente=models.CharField(max_length=45)
    estado=models.BooleanField(null=False)
    
    def __str__(self):
        return "{0}-{1}".format(self.fechaprestamo, self.nombrecliente)

class Ejemplar(models.Model):
    numeroejemplar=models.CharField(max_length=45)
    fechadecompra=models.DateField(null=False)
    Libro=models.ForeignKey('Libro', on_delete=models.CASCADE)

    def __str__(self):
        return self.numeroejemplar

class DetallePrestamo(models.Model):
    Prestamo=models.ForeignKey('Prestamo', on_delete=models.CASCADE)
    Ejemplar=models.ForeignKey('Ejemplar', on_delete=models.CASCADE)
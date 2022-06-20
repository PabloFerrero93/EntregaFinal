from django.db import models

class Perfil(models.Model):
    usuario=models.CharField(max_length=40)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    def __str__(self) -> str:
        return self.nombre+" "+ self.apellido

from django.db import models

# Create your models here.

class Generos(models.Model):
    id = models.AutoField(primary_key=True,db_column="genero_id")
    tipo_genero = models.CharField(max_length=50)

    class Meta:
        db_table = "generos"

class UsuariosProfile(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=255)
    fk_muchos = models.ManyToManyField(Generos)
    class Meta:
        db_table = "usuariosprofile"
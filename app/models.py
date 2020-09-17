from django.db import models

# Create your models here.
class Productos(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.FloatField(null=True)
    class Meta:
        db_table='productos'

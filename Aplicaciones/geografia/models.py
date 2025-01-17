from django.db import models

# Create your models here.
class Pais (models.Model):
    nombre= models.CharField(max_length=50)
    numero_habitantes=models.PositiveBigIntegerField()
    def __str__(self):
        return f'{self.nombre}'
    
class Ciudad(models.Model):
    nombre= models.CharField(max_length=100)
    alcalde=models.CharField(max_length=100)
    pais_id =models.ForeignKey(Pais,null=False,blank=False, on_delete= models.CASCADE)
    
    def __str__(self):
        return f'{self.nombre} {self.pais_id}'
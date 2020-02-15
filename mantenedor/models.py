from django.db import models

# Create your models here.
class Tipo_Rodamiento(models.Model):
    PK_TIPO_ROD = models.CharField(max_length=100, primary_key=True)
    TIPO = models.CharField(max_length=100,null=True)
    

class Rodamiento(models.Model):
    PK_ROD = models.AutoField(primary_key=True)
    D_INT_A = models.DecimalField(max_digits=15, decimal_places=5,null=True)
    D_INT_A1 = models.DecimalField(max_digits=15, decimal_places=5,null=True)
    D_EXT_D = models.DecimalField(max_digits=15, decimal_places=5,null=True)
    D_EXT_D1 = models.DecimalField(max_digits=15, decimal_places=5,null=True)
    D_ESP_B = models.DecimalField(max_digits=15, decimal_places=5,null=True)
    D_ESP_C = models.DecimalField(max_digits=15, decimal_places=5,null=True)
    D_ESP_T = models.DecimalField(max_digits=15, decimal_places=5,null=True)
    N_PARTE_1 = models.CharField(max_length=100,null=True)
    N_PARTE_2 = models.CharField(max_length=100,null=True)
    FK_TIPO_ROD = models.ForeignKey('Tipo_Rodamiento', on_delete=models.ProtectedError,null=True)
    DESCRIPCION = models.CharField(max_length=1000,null=True)

class Equivalente(models.Model):
    FK_RODAMIENTO = models.ForeignKey('Rodamiento',primary_key=True,unique=False, on_delete=models.CASCADE, null=False)
    N_ROD = models.CharField(max_length=100,null=True)
    MARCA = models.CharField(max_length=100,null=True)




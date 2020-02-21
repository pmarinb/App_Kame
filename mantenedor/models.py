from django.db import models

# Create your models here.


class Tipo_Rodamiento(models.Model):
    PK_TIPO_ROD = models.CharField(max_length=100, primary_key=True)
    TIPO = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.PK_TIPO_ROD + ' - ' + self.TIPO


class Rodamiento(models.Model):
    PK_ROD = models.AutoField(primary_key=True)
    D_INT_A = models.DecimalField(
        max_digits=15, decimal_places=5, default=0, blank=True, null=True)
    D_INT_A1 = models.DecimalField(
        max_digits=15, decimal_places=5, default=0, blank=True, null=True)
    D_EXT_D = models.DecimalField(
        max_digits=15, decimal_places=5, default=0, blank=True, null=True)
    D_EXT_D1 = models.DecimalField(
        max_digits=15, decimal_places=5, default=0, blank=True, null=True)
    D_ESP_B = models.DecimalField(
        max_digits=15, decimal_places=5, default=0, blank=True, null=True)
    D_ESP_C = models.DecimalField(
        max_digits=15, decimal_places=5, default=0, blank=True, null=True)
    D_ESP_T = models.DecimalField(
        max_digits=15, decimal_places=5, default=0, blank=True, null=True)
    N_PARTE_1 = models.CharField(max_length=100, blank=True)
    N_PARTE_2 = models.CharField(max_length=100, blank=True)
    FK_TIPO_ROD = models.ForeignKey(
        'Tipo_Rodamiento', on_delete=models.ProtectedError, blank=True, null=True)
    DESCRIPCION = models.CharField(max_length=1000, blank=True)


class Equivalente(models.Model):
    FK_RODAMIENTO = models.ForeignKey(
        'Rodamiento', on_delete=models.CASCADE, null=False)
    N_ROD = models.CharField(max_length=100, blank=True)
    MARCA = models.CharField(max_length=100, blank=True)

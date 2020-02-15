from django.contrib import admin
from .models import Equivalente, Rodamiento, Tipo_Rodamiento

# Register your models here.
admin.site.register(Equivalente)
admin.site.register(Rodamiento)
admin.site.register(Tipo_Rodamiento)
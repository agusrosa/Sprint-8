from django.contrib import admin
from .models import Dato
# Register your models here.
class DatosAdmin(admin.ModelAdmin):
    readonly_fields= ('actualizacion','creacion','saldo_cuenta')
admin.site.register(Dato)
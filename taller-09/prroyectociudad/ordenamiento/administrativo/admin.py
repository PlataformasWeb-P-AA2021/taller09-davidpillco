from django.contrib import admin

# Register your models here.
# Importar las clases del modelo
from administrativo.models import Parroquia, Barrio
from import_export.admin import ImportExportModelAdmin

class ParroquiaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nombre','tipo_parroquia')
admin.site.register(Parroquia, ParroquiaAdmin)


class BarrioAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nombre','num_viviendas','num_parques','num_edificios','parroquia')
admin.site.register(Barrio, BarrioAdmin)
from django.contrib import admin
from empleado.models import Empleado
from django.contrib.admin.helpers import Fieldset

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'usuario', 'numero_telefono', 'url', 'biografia', 'imagen')
    list_display_links = ('pk', 'usuario')
    list_editable = ('numero_telefono', 'url', 'biografia')
    search_fields = ('user__email', 'user__first_name', 'user__last_name', 'numero_telefono')
    list_filter = ('creado', 'modificado')
    fieldsets = ( ('Empleado', {
            'fields': (('usuario', 'imagen'),),
        }),
        ('Info extra', {
            'fields': (
                ('url', 'numero_telefono'),
                ('biografia')
            )
        }) 
    )


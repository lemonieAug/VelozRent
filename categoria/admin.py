from django.contrib import admin
from .models import Categoria

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('nome',)
        }
    list_display = ('nome','slug')

admin.site.register(Categoria, CategoriaAdmin)

from django.contrib import admin
from .models import Carro

# Register your models here.

class CarroAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('nome',)
        }
    list_display = ('nome','slug')

admin.site.register(Carro, CarroAdmin)
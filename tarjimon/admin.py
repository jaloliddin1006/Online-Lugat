from django.contrib import admin
from .models import Lugat
# Register your models here.

class LugatAdmin(admin.ModelAdmin):
    list_display = ['eng', 'uzb']
    
    
admin.site.register(Lugat, LugatAdmin)
from django.contrib import admin
from .models import Marker

# Register your models here.
class MarkerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Marker, MarkerAdmin)
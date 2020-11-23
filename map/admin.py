from django.contrib import admin
from .models import Marker, Monument, Photo

# Register your models here.
class MarkerAdmin(admin.TabularInline):
    model = Marker
    extra = 0

class PhotoAdmin(admin.TabularInline):
    model = Photo
    extra = 0
# admin.site.register(Marker, MarkerAdmin)

@admin.register(Monument)
class MonumentAdmin(admin.ModelAdmin):
    list_display = ("name", "state")
    
    inlines = [
        MarkerAdmin,
        PhotoAdmin
    ]

    def _markers(self, obj):
        return obj.markers.all().count()

    def _photos(self, obj):
        return obj.photos.all().count()

# admin.site.register(Monument, MonumentAdmin)
from django.contrib import admin
from .models import Marker, Monument, Photo

# Register your models here.
class MarkerInlineAdmin(admin.TabularInline):
    model = Marker

class MarkerAdmin(admin.ModelAdmin):
    model = Marker
    list_display = ("monument_name",)
    def monument_name(self, obj):
        return obj.monument.name

admin.site.register(Marker, MarkerAdmin)

class PhotoInlineAdmin(admin.TabularInline):
    model = Photo
    extra = 0

class PhotoAdmin(admin.ModelAdmin):
    model = Photo
    list_display = ("monument_name",)
    def monument_name(self, obj):
        return obj.monument.name

admin.site.register(Photo, PhotoAdmin)

@admin.register(Monument)
class MonumentAdmin(admin.ModelAdmin):
    list_display = ("name", "state")
    
    inlines = [
        PhotoInlineAdmin,
        MarkerInlineAdmin
    ]

    def _photos(self, obj):
        return obj.photos.all().count()

# admin.site.register(Monument, MonumentAdmin)
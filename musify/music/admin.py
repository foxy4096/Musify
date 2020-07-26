from django.contrib import admin
from .models import Music

# Register your models here.
class MusicAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc', 'date')



admin.site.register(Music, MusicAdmin)
admin.site.site_header ="Musify"
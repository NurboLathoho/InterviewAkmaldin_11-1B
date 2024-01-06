from django.contrib import admin
from .models import Settings
# Register your models here.
@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ['title', 'desc', 'image', 'price']
    list_filter = ['title', 'price']
    
    prepopulated_fields = {'slug': ('title', )}
from django.contrib import admin

from .models import Features
# Register your models here.

admin.site.register(Features)

class FeaturesAdmin(admin.ModelAdmin):
    fields = ['name', 'details']
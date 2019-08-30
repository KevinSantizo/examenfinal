from django.contrib import admin
from estate.models import Land, Plot, Tree
# Register your models here.


@admin.register(Land)
class LandAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'region')


@admin.register(Plot)
class PlotAdmin(admin.ModelAdmin):
    list_display = ('land', 'name', 'latitude', 'length')


@admin.register(Tree)
class TreeAdmin(admin.ModelAdmin):
    list_display = ('plot', 'diameter', 'height', 'health', 'year')

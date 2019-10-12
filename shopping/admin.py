from django.contrib import admin
from .models import Brand, Feature


class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'select')


class FeatureAdmin(admin.ModelAdmin):
    list_display = ('brand', 'make', 'price', 'body_style')


admin.site.register(Brand, BrandAdmin)
admin.site.register(Feature, FeatureAdmin)

# Register your models here.

from __future__ import absolute_import
from django.contrib import admin

from .models import Facility, Hcc, Nhcs

class FacilityModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created']
    list_filter = ('name', 'created',)
    search_fields = ('name',)

    class Meta:
        model = Facility
admin.site.register(Facility, FacilityModelAdmin)

class HccModelAdmin(admin.ModelAdmin):
    list_display = ['representative', 'position', 'created']
    list_filter = ('representative', 'position', 'created',)
    search_fields = ('representative', 'position', 'created',)

    class Meta:
        model = Hcc
admin.site.register(Hcc, HccModelAdmin)

class NhcsModelAdmin(admin.ModelAdmin):
    list_display = ['representative', 'position', 'created']
    list_filter = ('representative', 'position', 'created',)
    search_fields = ('representative', 'position', 'created',)

    class Meta:
        model = Nhcs
admin.site.register(Nhcs, NhcsModelAdmin)

from django.contrib import admin

from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

from HierarchyApp.models import Monitor

admin.site.register(Monitor, DraggableMPTTAdmin)
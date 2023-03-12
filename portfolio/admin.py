from django.contrib import admin
from .models import *

class BioAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return True

class IdenticAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return True

admin.site.register(Project)
admin.site.register(Bio, BioAdmin)
admin.site.register(Link)
admin.site.register(Identic, IdenticAdmin)

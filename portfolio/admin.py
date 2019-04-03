from django.contrib import admin
from . import models

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(models.Project, ProjectAdmin)
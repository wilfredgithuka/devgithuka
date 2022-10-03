## Django modules

from django.contrib import admin

##App modules

from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('author','title','created_on','budget')

admin.site.register(Project, ProjectAdmin)

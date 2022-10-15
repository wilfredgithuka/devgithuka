## Django modules

from django.contrib import admin

##App modules

from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','created_on','budget','progress')

admin.site.register(Project, ProjectAdmin)

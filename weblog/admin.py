## Django modules

from django.contrib import admin

##App modules

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('author','title','created_on','status','project')

admin.site.register(Post, PostAdmin)

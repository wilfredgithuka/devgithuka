from django.urls import path

# Specifies the app name for name spacing.
app_name = 'weblog'

# Blog application imports.
from weblog.views import (
    PostListView,
    PostDetailView,
    PostSearchListView,
)

# post/urls.py
urlpatterns = [

    # POST URLS #

    # /home/
    path(
        route='',
        view=PostListView.as_view(),
        name='post_list'
    ),

    path(
        route='<str:slug>/',
        #route='<str:slug>/',
        view=PostDetailView.as_view(),
        name='post_detail'
    ),

    path(
         route='post/search/',
         view=PostSearchListView.as_view(),
         name='post_search_list'

     ),]

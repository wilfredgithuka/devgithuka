from django.urls import path

# Specifies the app name for name spacing.
app_name = 'projects'

# Blog application imports.
from projects.views import (
    ProjectListView,
    ProjectDetailView,
    #ProjectSearchListView,
)

# Project/urls.py
urlpatterns = [

    # Project URLS #

    # /home/
    path(
        route='',
        view=ProjectListView.as_view(),
        name='projects_list'
    ),

    path(
        route='<str:slug>/',
        #route='<str:slug>/',
        view=ProjectDetailView.as_view(),
        name='projects_detail'
    ),]

    # path(
    #      route='project/search/',
    #      view=ProjectSearchListView.as_view(),
    #      name='project_search_list'

    #  ),]

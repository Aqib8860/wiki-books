from django.urls import path

from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("wiki/<str:title>",views.wiki, name="wiki"),
    path("search",views.search, name="search"),
    path("new_page",views.new_page, name="new_page"),
    path("edit_page/<str:title>",views.edit_page, name="edit_page"),
    path("random_page", views.random_page , name="random_page")
]

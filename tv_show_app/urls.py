from django.urls import path
from . import views

urlpatterns = [
    path("go_back/", views.index),
    path("", views.index),
    path("shows/", views.view_shows),
    path("shows/new/", views.add_new_show_page),
    path("shows/create/", views.create_show),  # creating of show and adding to DB
    path("shows/<int:show_id>/", views.view_show_details),
    path("shows/<int:show_id>/delete", views.delete_show),
    path("shows/<int:show_id>/edit/", views.edit_show_page),
    path("shows/<int:show_id>/update/", views.update_show),
]
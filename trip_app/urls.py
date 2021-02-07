from django.urls import path
from . import views	# the . indicates that the views file can be found in the same directory as this file
                    
urlpatterns = [
    path('', views.index),
    path('dashboard', views.dashboard),
    path('register',views.register),
    path('login', views.login),
    path('trip/new', views.shows_new),
    path('create', views.create),
    # path('shows/<int:id>', views.display_show),
    path('trip/<int:id>/edit', views.edit),
    path('trip/<int:id>/update', views.update),
    path('trip/<int:id>/delete', views.delete),
    path('logout', views.logout),
    path('trip/<int:id>', views.display_show),
]
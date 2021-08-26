from django.urls import path

from . import views

app_name = 'players'
urlpatterns = [
    path('', views.index, name='index'),
    path('playerdetail/<str:player_id>/',views.playerdetail, name='playerdetail'),
    path('createplayer/',views.createplayer, name='createplayer'),
    path('save/', views.save, name='save'),
]
from django.urls import path

from . import views

app_name = 'teams'
urlpatterns = [
    path('', views.index, name='index'),
    path('teamdetail/<str:team_id>/',views.teamdetail, name='teamdetail'),
    path('createteam/',views.createteam, name='createteam'),
    path('save/', views.save, name='save'),
]
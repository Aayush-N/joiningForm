from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('done/', views.done, name='done'),
    path('display/', views.DisplayView.as_view(), name='display'),
]
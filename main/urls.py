from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('signup/', views.register, name='signup'),
    path('apply/', views.PositionView.as_view(), name='index'),
    path('done/', views.done, name='done'),
    path('display/', views.DisplayView.as_view(), name='display'),
    path('download/', views.ExportView, name='download'),
    path('personal/', views.PersonalView.as_view(), name='personal'),
    path('educational/', views.EducationalView.as_view(), name='educational'),
    path('teaching/', views.TeachingView.as_view(), name='teaching'),
    path('industrial/', views.IndustrialView.as_view(), name='industrial'),
    path('research/', views.ResearchView.as_view(), name='research'),
    path('conference/', views.ConferenceView.as_view(), name='conference'),
    path('payment/', views.PaymentView.as_view(), name='payment'),
    path('documents/', views.DocumentsView.as_view(), name='documents'),

]



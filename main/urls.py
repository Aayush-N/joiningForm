from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('apply/', views.PositionView.as_view(), name='index'),
    path('done/', views.done, name='done'),
    path('display/', views.DisplayView.as_view(), name='display'),
    path('download/', views.ExportView, name='download'),
    path('personal/', views.personalView.as_view(), name='personal'),
    path('educational/', views.educationalView.as_view(), name='educational'),
    path('professional/', views.professionalView.as_view(), name='professional'),
    path('payment/', views.paymentView.as_view(), name='payment'),
    path('documents/', views.documentsView.as_view(), name='documents'),
    path('login/', views.LoginView.as_view(), name='login'),

]



from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('apply/', views.PositionView.as_view(), name='index'),
    path('done/', views.done, name='done'),
    path('display/', views.DisplayView.as_view(), name='display'),
    path('export/', views.download_select_view, name='download report'),
    path('download/<file>/', views.export_view, name='download'),
    path('personal/', views.PersonalView.as_view(), name='personal'),
    path('educational/', views.EducationalView.as_view(), name='educational'),
    path('teaching/', views.TeachingView.as_view(), name='teaching'),
    path('industrial/', views.IndustrialView.as_view(), name='industrial'),
    path('research/', views.ResearchView.as_view(), name='research'),
    path('membership/', views.MembershipView.as_view(), name='membership'),
    path('conference/', views.ConferenceView.as_view(), name='conference'),
    path('awards/', views.AwardsView.as_view(), name='awards'),
    path('reference/', views.ReferenceView.as_view(), name='reference'),
    path('achievement/', views.AchievementView.as_view(), name='achievement'),
    path('payment/', views.PaymentView.as_view(), name='payment'),
    path('documents/', views.DocumentsView.as_view(), name='documents'),
    path('declaration/', views.DeclarationView.as_view(), name='declaration'),
    path('print/', views.printView, name='print'),
    path('admin-print/<email>/', views.admin_print_view, name='admin-print'),
    path('do_declare/',views.declaration, name='decl'),
]



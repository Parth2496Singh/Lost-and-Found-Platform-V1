from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path('report-lost/', views.report_lost, name='report_lost'),
    path('report-found/', views.report_found, name='report_found'),
    path('search/', views.search, name='search'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path("lost/<int:id>/", views.lost_detail, name="lost_detail"),
    path("found/<int:id>/", views.found_detail, name="found_detail"),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-of-service/', views.terms_of_service, name='terms_of_service')

]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscription_page, name='subscription_page'),
    path('subscribe/<int:app_id>/', views.subscribe, name='subscribe'),
    path('unsubscribe/<int:app_id>/', views.unsubscribe, name='unsubscribe'),
]

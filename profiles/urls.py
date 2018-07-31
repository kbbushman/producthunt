from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.profile, name='profile'),
    path('<int:pk>/edit/', views.profile_edit, name='profile_edit'),
    path('<int:pk>/delete/', views.profile_delete, name='profile_delete'),
]

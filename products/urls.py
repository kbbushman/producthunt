from django.urls import path, include
from . import views

urlpatterns = [
    path('new/', views.create, name='product_new'),
    path('<int:product_id>', views.show, name='product_detail'),
    path('<int:product_id>/upvote', views.upvote, name='upvote'),
]

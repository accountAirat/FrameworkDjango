from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all/', views.all_users, name='all'),
    path('get_user_ordered_products/<int:user_id>/', views.get_user_ordered_products, name='get_user_ordered_products'),
]

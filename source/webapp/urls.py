from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('task/<int:pk>', views.detail, name='detail'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete-items/', views.delete_items, name='delete_items')
]

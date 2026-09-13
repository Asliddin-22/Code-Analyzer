from django.contrib import admin
from django.urls import path
from analyzer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('sessions/', views.submission_list, name='submission_list'),
    path('sessions/<int:pk>/', views.submission_detail, name='submission_detail'),
    path('delete/<int:pk>/', views.delete_submission, name='delete_submission'),
]

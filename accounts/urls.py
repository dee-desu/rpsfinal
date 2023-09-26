from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.project_list, name='project_list'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('projects/create/', views.project_create, name='project_create'),
    path('projects/<int:project_id>/edit/', views.project_edit, name='project_edit'),
    path('projects/<int:project_id>/delete/', views.project_delete, name='project_delete'),
    #Banner images urls:
    path('banner-images/', views.banner_image_list, name='banner_image_list'),
    path('banner-images/upload/', views.upload_banner_image, name='upload_banner_image'),
    path('banner-images/delete/<int:image_id>/', views.delete_banner_image, name='delete_banner_image'),
    #Logo images urls:
    path('logo-images/', views.logo_image_list, name='logo_image_list'),
    path('logo-images/upload/', views.upload_logo_image, name='upload_logo_image'),
    path('logo-images/delete/<int:image_id>/', views.delete_logo_image, name='delete_logo_image'),
]

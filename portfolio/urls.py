from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .api import BannerViewSet, ProjectViewSet,LogoViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'banners', BannerViewSet, basename='banner')
router.register(r'logos', LogoViewSet, basename='logos')

urlpatterns = [
    path('api/', include(router.urls)),

    path('', views.project_list, name='project_list'),
    path('<int:project_id>/', views.project_detail, name='project_detail'),
    path('create/', views.project_create, name='project_create'),
    path('<int:project_id>/edit/', views.project_edit, name='project_edit'),
    path('delete/<int:project_id>/', views.project_delete, name='project_delete'),
    path('banner-images/', views.banner_image_list, name='banner_image_list'),
    path('banner-images/upload/', views.upload_banner_image, name='upload_banner_image'),
    path('banner-images/delete/<int:image_id>/', views.delete_banner_image, name='delete_banner_image'),
    #clients logos:
    path('logo-images/', views.logo_image_list, name='logo_image_list'),
    path('logo-images/upload/', views.upload_logo_images, name='upload_logo_images'),
    path('logo-images/delete/<int:image_id>/', views.delete_logo_images, name='delete_logo_images')

]


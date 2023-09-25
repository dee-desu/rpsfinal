from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .api import BannerViewSet, ProjectViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'banners', BannerViewSet, basename='banner')

urlpatterns = [
    path('api/', include(router.urls)),

    path('', views.project_list, name='project_list'),
    path('<int:project_id>/', views.project_detail, name='project_detail'),
    path('create/', views.project_create, name='project_create'),
    path('<int:project_id>/edit/', views.project_edit, name='project_edit'),
    path('<int:project_id>/delete/', views.project_delete, name='project_delete'),
    # path('projects/', views.project_list, name='project_list'),
    # path('projects/', ProjectViewSet.as_view(), name='project_list'),
    path('banner-images/', views.banner_image_list, name='banner_image_list'),
    path('banner-images/upload/', views.upload_banner_image, name='upload_banner_image'),
    path('banner-images/delete/<int:image_id>/', views.delete_banner_image, name='delete_banner_image'),
]

# from .api import ProjectListByCategory, ProjectImageList, ProjectListByCategoryAPIView,BannerImageListAPIView
# urlpatterns += [
#     path('api/projects/<int:pk>/', ProjectDetailAPIView.as_view(), name='project-detail'),
#     path('api/projects/', ProjectListAPIView.as_view(), name='project-list'),
#     path('api/projects/category/', ProjectListByCategoryAPIView.as_view(), name='project-list-by-category'),
#     path('api/projects/<str:category_name>/', ProjectListByCategory.as_view(), name='project-list-by-category'),
#     path('api/projects/<int:project_id>/images/', ProjectImageList.as_view(), name='project-image-list'),
#     path('api/banner-images/', BannerImageListAPIView.as_view(), name='banner-image-list'),
# ]

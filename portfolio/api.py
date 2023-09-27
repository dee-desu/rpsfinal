from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.db.models import Q
from .models import Project, BannerImage, LogoImages
from .serializers import ProjectSerializer, BannerImageSerializer, LogoImageSerializer


class ProjectViewSet(ModelViewSet):
    permission_classes=[AllowAny]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        category_name = self.request.query_params.get("category_name", None)
        category_id = self.request.query_params.get("category_id", None)
        if not category_name and not category_id :
            return self.queryset
        
        query = self.queryset.filter(
            Q (category__catname=category_name) |
            Q (category__id=category_id)
        )

        return query
    

class BannerViewSet(ModelViewSet):
    permission_classes=[AllowAny]
    queryset = BannerImage.objects.all()
    serializer_class = BannerImageSerializer

class LogoViewSet(ModelViewSet):
    permission_classes=[AllowAny]
    queryset = LogoImages.objects.all()
    serializer_class = LogoImageSerializer    

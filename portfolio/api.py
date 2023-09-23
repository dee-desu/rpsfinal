from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ModelViewSet

from .models import Project, BannerImage
from .serializers import ProjectSerializer, BannerImageSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        category_name = self.request.query_params.get("category_name", None)
        category_id = self.request.query_params.get("category_id", None)
        query = self.queryset.filter(category__catname=category_name) if category_name is not None else self.queryset
        query = self.queryset.filter(category__id=category_id) if category_id is not None else query

        return query

    def create(self, request, *args, **kwargs):
        images = request.data.pop("images") if 'images' in request.data else None
        serializer = self.get_serializer(data=request.data, context={'request': request, 'images': images})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            error_message = str(serializer.errors)
            return Response({'message': error_message}, status=HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        images = request.data.pop("images") if 'images' in request.data else None

        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial,
                                         context={'request': request, 'images': images})

        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            error_message = str(serializer.errors)
            return Response({'message': error_message}, status=HTTP_400_BAD_REQUEST)


class BannerViewSet(ModelViewSet):
    queryset = BannerImage.objects.all()
    serializer_class = BannerImageSerializer

# from .models import ProjectImage, Category
# from rest_framework import generics
# from rest_framework.generics import get_object_or_404
# from rest_framework.response import Response
# from .serializers import ProjectListSerializer, ProjectImageSerializer


# class ProjectDetailAPIView(generics.RetrieveAPIView):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer
#
#
# class BannerImageListAPIView(generics.ListAPIView):
#     queryset = BannerImage.objects.all()
#     serializer_class = BannerImageSerializer
#
#
# class ProjectListByCategoryAPIView(generics.ListAPIView):
#     serializer_class = ProjectSerializer
#
#     def get_queryset(self):
#         category_name = self.request.data.get('category_name')
#         if category_name:
#             return Project.objects.filter(category__name=category_name)
#         else:
#             return Project.objects.all()
#
#     def get_serializer(self, *args, **kwargs):
#         # Customize the serializer to include project images
#         kwargs['context'] = self.get_serializer_context()
#         return ProjectSerializer(*args, **kwargs)
#
#     def list(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def create(self, request, *args, **kwargs):
#         # Deserialize locations as an array
#         locations = request.data.get('locations', [])
#         request.data['locations'] = locations
#         return super().create(request, *args, **kwargs)
#
#
# class ProjectImageList(generics.ListAPIView):
#     serializer_class = ProjectImageSerializer
#
#     def get_queryset(self):
#         # Retrieve the project ID from the URL parameter
#         project_id = self.kwargs['project_id']
#
#         # Filter and return the images related to the specified project
#         return ProjectImage.objects.filter(project_id=project_id)
#
#     class ProjectListByCategory(generics.ListAPIView):
#         serializer_class = ProjectListSerializer
#
#         def get_queryset(self):
#             # Retrieve the category name from the URL parameter
#             category_name = self.kwargs['category_name']
#
#             # Get the category object or return a 404 if it doesn't exist
#             category = get_object_or_404(Category, catname=category_name)
#
#             # Filter and return the projects in the specified category
#             return Project.objects.filter(category=category)

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
import json
from .models import Category, Project, ProjectImage, BannerImage, LogoImages
import re

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'  # You can specify which fields to include if needed


class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ('id', 'image')


class ProjectSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  # Use the CategorySerializer for the related field

    images = ProjectImageSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'



    def to_representation(self, instance):
        # Serialize locations as an array
        representation = super().to_representation(instance)
        representation['locations'] = [re.sub(r'[^0-9a-zA-Z/-]', '', x) for x in instance.locations]
        return representation

  

class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'date', 'thumbnail', 'category')


class BannerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerImage
        fields = ('image',)

class LogoImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogoImages
        fields = ('image',)


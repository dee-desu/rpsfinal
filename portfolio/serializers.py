from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from .models import Category, Project, ProjectImage, BannerImage


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
    category_id = serializers.IntegerField(write_only=True)
    images = ProjectImageSerializer(many=True, required=False)

    class Meta:
        model = Project
        fields = '__all__'

    def to_representation(self, instance):
        # Serialize locations as an array
        representation = super().to_representation(instance)
        representation['locations'] = instance.locations
        return representation

    def create(self, validated_data):
        category_id = validated_data.pop('category_id', None)
        locations = eval(validated_data.pop('locations', ["None"])[0])
        images_list = self.context.get("images", None)
        if category_id is not None:
            try:
                category = Category.objects.get(id=category_id)
            except ObjectDoesNotExist:
                raise serializers.ValidationError(f"There is no category with id {category_id}")
        else:
            category = None

        project = Project.objects.create(category=category, locations=locations, **validated_data)
        print(f"{images_list = }")
        if images_list is not None:
            ProjectImage.objects.bulk_create([
                ProjectImage(project=project, image=img) for img in images_list
            ])

        return project

    def update(self, instance, validated_data):
        category_id = validated_data.pop('category_id', None)
        locations = eval(validated_data.pop('locations', ["None"])[0])
        images_list = self.context.get("images", None)
        name = validated_data.get("name", None)
        date = validated_data.get("date", None)
        description = validated_data.get("description", None)
        thumbnail = validated_data.get("thumbnail", None)
        if category_id is not None:
            try:
                category = Category.objects.get(id=category_id)
            except ObjectDoesNotExist:
                raise serializers.ValidationError(f"There is no category with id {category_id}")
        else:
            category = None

        if not self.partial:
            if any([
                category is None,
                name is None,
                date is None,
                description is None,
            ]):
                raise serializers.ValidationError("Not all required field exists")
        instance.name = name or instance.name
        instance.date = date or instance.date
        instance.description = description or instance.description
        instance.category = category or instance.category
        instance.thumbnail = thumbnail or instance.thumbnail if self.partial else thumbnail
        instance.locations = locations or instance.locations if self.partial else locations
        if images_list is not None or not self.partial:
            instance.images.all().delete()
            if images_list is not None:
                ProjectImage.objects.bulk_create([
                    ProjectImage(project=instance, image=img) for img in images_list
                ])

        instance.save()
        return instance


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'date', 'thumbnail', 'category')


class BannerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerImage
        fields = ('image',)

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from portfolio.models import Project, BannerImage, ProjectImage, LogoImages
from portfolio.forms import ProjectForm, BannerImageForm, LogoImagesForm



@api_view(['GET'])
@csrf_exempt
@login_required
def project_list(request):
    """
    Retrieve a list of all projects.
    """
    projects = Project.objects.all()
    project_data = []

    for project in projects:
        project_images = project.images.all()
        image_data = [{'id': image.id, 'image_url': request.build_absolute_uri(image.image.url)} for image in project_images]

        project_data.append({
            'id': project.id,
            'name': project.name,
            'date': project.date,
            'category': project.category.catname,
            'description': project.description,
            'thumbnail_url': request.build_absolute_uri(project.thumbnail.url) if project.thumbnail else None,
            'locations': project.locations,
            'images': image_data,
        })

    return JsonResponse({'projects': project_data})

@api_view(['GET'])
@csrf_exempt
@login_required
def project_detail(request, project_id):
    """
    Retrieve details of a specific project.
    """
    project = get_object_or_404(Project, id=project_id)
    project_images = project.images.all()
    image_data = [{'id': image.id, 'image_url': request.build_absolute_uri(image.image.url)} for image in project_images]

    project_data = {
        'id': project.id,
        'name': project.name,
        'date': project.date,
        'category': project.category.catname,
        'description': project.description,
        'thumbnail_url': request.build_absolute_uri(project.thumbnail.url) if project.thumbnail else None,
        'locations': project.locations,
        'images': image_data,
    }

    return JsonResponse({'project': project_data})

@api_view(['POST'])
@csrf_exempt
@login_required
def project_create(request):
    """
    Create a new project.
    """
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)

            # Process and save the project data
            project.save()

            # Process and save the uploaded images
            for image in request.FILES.getlist('images'):
                project_image = ProjectImage(project=project, image=image)
                project_image.save()

            return JsonResponse({'message': 'Project created successfully'})
        else:
            return JsonResponse({'error': 'Invalid form data'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

@api_view(['PUT'])
@csrf_exempt
@login_required
def project_edit(request, project_id):
    """
    Edit an existing project.
    """
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'PUT':
        form = ProjectForm(request.data, instance=project)
        if form.is_valid():
            project = form.save()

            # Clear existing project images and re-save the uploaded images
            ProjectImage.objects.filter(project=project).delete()
            for image in request.FILES.getlist('images'):
                project_image = ProjectImage(project=project, image=image)
                project_image.save()

            return JsonResponse({'message': 'Project updated successfully'})
        else:
            return JsonResponse({'error': 'Invalid form data'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

@api_view(['DELETE'])
@csrf_exempt
@login_required
def project_delete(request, project_id):
    """
    Delete an existing project.
    """
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'DELETE':
        project.delete()
        return JsonResponse({'message': 'Project deleted successfully'})

@api_view(['GET'])
@csrf_exempt
@login_required
def banner_image_list(request):
    """
    Retrieve a list of all banner images.
    """
    banner_images = BannerImage.objects.all()
    banner_data = [{'id': image.id, 'image_url': image.image.url} for image in banner_images]

    return JsonResponse({'banner_images': banner_data})

@api_view(['POST'])
@csrf_exempt
@login_required
def upload_banner_image(request):
    """
    Upload a new banner image.
    """
    if request.method == 'POST':
        form = BannerImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Banner image uploaded successfully'})
        else:
            return JsonResponse({'error': 'Invalid form data'}, status=400)

@api_view(['DELETE'])
@csrf_exempt
@login_required
def delete_banner_image(request, image_id):
    """
    Delete a specific banner image.
    """
    image = get_object_or_404(BannerImage, id=image_id)
    if request.method == 'DELETE':
        image.delete()
        return JsonResponse({'message': 'Banner image deleted successfully'})


@api_view(['GET'])
@csrf_exempt
@login_required
def logo_image_list(request):
    """
    Retrieve a list of all logo images.
    """
    logo_images = LogoImages.objects.all()
    logo_data = [{'id': image.id, 'image_url': image.image.url} for image in logo_images]

    return JsonResponse({'logo_images': logo_data})

@api_view(['POST'])
@csrf_exempt
@login_required
def upload_logo_image(request):
    """
    Upload a new logo image.
    """
    if request.method == 'POST':
        form = LogoImagesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Logo image uploaded successfully'})
        else:
            return JsonResponse({'error': 'Invalid form data'}, status=400)

@api_view(['DELETE'])
@csrf_exempt
@login_required
def delete_logo_image(request, image_id):
    """
    Delete a specific logo image.
    """
    image = get_object_or_404(LogoImages, id=image_id)
    if request.method == 'DELETE':
        image.delete()
        return JsonResponse({'message': 'Logo image deleted successfully'})
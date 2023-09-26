from django.shortcuts import render, redirect, get_object_or_404

from .forms import ProjectForm, BannerImageForm,LogoImagesForm
from .models import Project, ProjectImage, BannerImage,LogoImages
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework.permissions import AllowAny

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/project_list.html', {'projects': projects})


def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'portfolio/project_detail.html', {'project': project})


def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            # Create a new project instance and populate it with form data
            project = form.save(commit=False)

            # Process the location data (assuming locations are comma-separated)
            location_data = request.POST.getlist('locations')
            project.locations = ', '.join(location_data)

            project.save()

            # Process and save the uploaded images
            for image in request.FILES.getlist('images'):
                project_image = ProjectImage(project=project, image=image)
                project_image.save()

            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'portfolio/project_form.html', {'form': form})


def project_edit(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            # Update the project instance and populate it with form data
            project = form.save(commit=False)

            # Process the location data (assuming locations are comma-separated)
            location_data = request.POST.getlist('locations')
            project.locations = ', '.join(location_data)

            project.save()

            # Clear existing project images and re-save the uploaded images
            ProjectImage.objects.filter(project=project).delete()
            for image in request.FILES.getlist('images'):
                project_image = ProjectImage(project=project, image=image)
                project_image.save()

            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'portfolio/project_form.html', {'form': form})


def project_delete(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    return render(request, 'portfolio/project_confirm_delete.html', {'project': project})


# Banner methods

def banner_image_list(request):
    banner_images = BannerImage.objects.all()

    return render(request, 'your_template/banner_image_list.html', {'banner_images': banner_images})


def upload_banner_image(request):
    if request.method == 'POST':
        form = BannerImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('banner_image_list')
    else:
        form = BannerImageForm()
    return render(request, 'your_template/upload_banner_image.html', {'form': form})


def delete_banner_image(request, image_id):
    image = get_object_or_404(BannerImage, id=image_id)
    if request.method == 'POST':
        image.delete()
    return redirect('banner_image_list')


# Logo slider


def logo_image_list(request):
    logo_images = LogoImages.objects.all()

    return render(request, 'your_template/logo_image_list.html', {'logo_images': logo_images})


def upload_logo_images(request):
    if request.method == 'POST':
        form = LogoImagesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('logo_image_list')
    else:
        form = LogoImagesForm()
    return render(request, 'your_template/upload_logo_images.html', {'form': form})


def delete_logo_images(request, image_id):
    image = get_object_or_404(LogoImages, id=image_id)
    if request.method == 'POST':
        image.delete()
    return redirect('logo_image_list')
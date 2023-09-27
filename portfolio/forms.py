from django import forms
from .models import Project,BannerImage,LogoImages

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"

    # Define widgets and form field options here


class BannerImageForm(forms.ModelForm):
    class Meta:
        model = BannerImage
        fields = ['image']

class LogoImagesForm(forms.ModelForm):
    class Meta:
        model = LogoImages
        fields = ['image']
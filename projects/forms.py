from django.forms import ModelForm
from .models import Project, Review, Tag

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        exclude = ['owner', 'vote_total', 'vote_ratio'] # Exclude fields that should not be set by the user directly
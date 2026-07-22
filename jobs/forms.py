from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company_name', 'description', 'location', 'salary']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Senior Python Developer'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. TechCorp Inc.'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Describe job duties, requirements, benefits...'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. New York, NY / Remote'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 95000'}),
        }
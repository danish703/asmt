from django import forms
from .models import Employee,Experience,Skill
class EmployeForm(forms.ModelForm):
    fullname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    contact_no = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    qualification = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    website = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}))
    class Meta:
        model=Employee
        exclude = ['user']


class EmployeEditForm(forms.ModelForm):
    fullname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    contact_no = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    qualification = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    website = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}))
    class Meta:
        model=Employee
        exclude = ['user','profile_img']


class EmployeImageEditForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields = ['profile_img']


class ExperineceForm(forms.ModelForm):
    company_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    duration = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    designation = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model=Experience
        exclude = ['employee']



class SkillForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=Skill
        exclude = ['employee']




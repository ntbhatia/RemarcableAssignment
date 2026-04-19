from django import forms
from .models import Category, Tag

class ProductFilterForm(forms.Form):

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(), 
        required=False, 
        empty_label='All Categories'
        )
    
    tag = forms.ModelChoiceField(
        queryset=Tag.objects.all(), 
        required=False, 
        empty_label='All Tags'
        )
    
    search = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Search Products'})
        )
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment  # Define the model here
        fields = ('name', 'email', 'body')  # Specify the fields

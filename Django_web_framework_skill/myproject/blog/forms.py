from django import forms
from .models import Comment
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']  # don’t include author/created_at
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Write your content here...'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']

from django import forms
from .models import Post
from .models import Comment 
from .models import Place

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('user', 'email', 'body')

class PlaceForm(forms.ModelForm):
	class Meta:
		model = Place
		fields = ('name', 'parametr', 'text')

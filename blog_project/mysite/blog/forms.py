from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from blog.models import Post,Comment

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('author','title','text')
        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }
        
class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('author','text')
        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=40, required=True, help_text='Required')
    last_name = forms.CharField(max_length=40, required=True, help_text='Required')
    email = forms.EmailField(max_length=254, help_text='Required')
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
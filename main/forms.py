from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from main.models import Blog, Comment, Profile


class BlogCreateForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Blog
        exclude = ['author']

        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }


class BlogUpdateForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    picture = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Blog
        exclude = ['author']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label='Email')
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Name')
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}),
                                label='Surname')
    username = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Username')
    password1 = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                label='Password')
    password2 = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                label='Password confirmation')

    # bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class UserForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label='Email')
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Name')
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}),
                                label='Surname')
    username = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Username')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    birth = forms.DateField(widget=forms.DateInput(
        attrs={'class': 'form-control',
               'placeholder': 'Select a date',
               'type': 'date',
               }), label='Date of birth')
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label="About", max_length=500,
                          required=False)

    class Meta:
        model = Profile
        fields = ('birth', 'bio')

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from grappelli.templatetags.grp_tags import User


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='User name', widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='User password', widget=forms.TextInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='User password', widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='User name', widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='User password', widget=forms.TextInput(attrs={'class':'form-control'}))




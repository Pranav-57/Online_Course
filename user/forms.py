from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, authenticate, UserChangeForm

class Registration(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('name','email','password1','password2')  

class loginform(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('email','password')    

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Invalid Login')

class ProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = CustomUser
        fields = ('name','user_image','position','description')
        labels = {
            'position':'Role',
            'description':'About Yourself'
        }
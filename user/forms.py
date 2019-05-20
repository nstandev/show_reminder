from django import forms
from django.contrib.auth.models import User
from django.forms import PasswordInput
from django.contrib.auth import get_user_model, authenticate


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=PasswordInput)
    password2 = forms.CharField(widget=PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'password2', 'username']


class UserLoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    # username = forms.CharField()

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Password is incorrect')
            if not user.is_active:
                raise forms.ValidationError('user is not active')

            super(UserLoginForm, self).clean(*args, **kwargs)

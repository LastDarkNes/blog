from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=12)
    email = forms.EmailField()
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)


class AuthorizationForm(forms.Form):
    username = forms.CharField(max_length=12)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
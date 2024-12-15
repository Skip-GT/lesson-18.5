from django import forms


class UserRegister(forms.Form):
    username = forms.CharField(label='Введите логин', max_length=30)
    password = forms.CharField(label='Введите пароль', min_length=8, widget=forms.PasswordInput)
    repeat_password = forms.CharField(label='Повторите пароль', min_length=8, widget=forms.PasswordInput)
    age = forms.IntegerField(label='Введите свой возраст', min_value=18, max_value=150)

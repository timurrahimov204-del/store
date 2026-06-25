from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Profile
from orders.models import User

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Логин', max_length=28, required=True)
    first_name = forms.CharField(label='Имя', min_length=1, max_length=28, required=True)
    last_name = forms.CharField(label='Фамилия', min_length=1, max_length=28, required=False)
    birth_date = forms.DateField(label='Дата рождения', required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    tel = forms.CharField(label='Телефон', max_length=20, required=True)
    email = forms.EmailField(label='Email', max_length=128, required=True)
    address = forms.CharField(label='Страна', max_length=28, required=True)
    gender = forms.CharField(label='Пол(м, ж)', max_length=1, required=False)
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput, required=True)


    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.address = self.cleaned_data['address']
        user.gender = self.cleaned_data['gender']
        
        if commit:
            user.save()
            profile = Profile.objects.get(usrr=user)
            profile.birth_date = self.cleaned_data.get('birth_date')
            profile.tel = self.cleaned_data.get('tel')
            profile.save()
        
        return user
    

            

            

    

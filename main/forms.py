from django import forms
from main.models import Meal
from users.models import CustomUser


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('height', 'weight', 'sex', 'birth_date')
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }


class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = "__all__"
        exclude = ['user', 'timestamp']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

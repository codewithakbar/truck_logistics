from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "father_name",
            "birthday_date",
            "gender",
            "phone_number",
            "user_type",
        )
        widgets = {
            "birthday_date": forms.DateInput(attrs={"type": "date"}),
        }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "father_name",
            "birthday_date",
            "gender",
            "phone_number",
            "user_type",
        ]
        
        widgets = {
            "birthday_date": forms.DateInput(attrs={"type": "date"}),
        }



class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    phone_number = forms.CharField(max_length=20, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'phone_number', 'password1', 'password2']
        
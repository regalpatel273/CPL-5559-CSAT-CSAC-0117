from .models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from captcha.fields import CaptchaField


class DateInput(forms.DateInput):
    input_type = 'date'

class MyUserCreationForm(UserCreationForm):
    date_of_birth = forms.DateField(widget=DateInput)
    phone_number = PhoneNumberField(
        widget = PhoneNumberPrefixWidget()
    )
    captcha = CaptchaField()
    class Meta:
        model = User
        fields = ['email','username','first_name','last_name','password1','password2','date_of_birth','phone_number','bio', 'avatar']


class UserForm(UserCreationForm):
    date_of_birth = forms.DateField(widget=DateInput)
    phone_number = PhoneNumberField(
        widget = PhoneNumberPrefixWidget()
    )
    class Meta:
        model = User
        fields = ['email','username','first_name','last_name','password1','password2','date_of_birth','phone_number','bio', 'avatar']


class UserAdminForm(UserCreationForm):
    date_of_birth = forms.DateField(widget=DateInput)
    phone_number = PhoneNumberField(
        widget = PhoneNumberPrefixWidget()
    )
    class Meta:
        model = User
        fields = ['email','username','first_name','last_name','password1','password2','date_of_birth','phone_number','bio', 'avatar','department','head_of_department']

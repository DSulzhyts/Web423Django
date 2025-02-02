from django import forms
from django.core.exceptions import ValidationError

from users.models import User
from users.validators import validate_password


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserRegisterForm(StyleFormMixin, forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput, min_length=6, max_length=12,
                               help_text='От 6 до 12 букв латинского алфавита и/или цифр')
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'avatar',)

    def clean_password2(self):
        temp_data = self.cleaned_data
        validate_password(temp_data['password'])
        if temp_data['password'] != temp_data['password2']:
            print('Пароли не совпадают')
            raise ValidationError('Пароли не совпадают')
        return temp_data['password2']


class UserLoginForm(StyleFormMixin, forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserUpdateForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'telegram', )

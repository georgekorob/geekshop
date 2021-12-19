import hashlib
import random

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.core.exceptions import ValidationError

from authapp.models import UserProfile
from authapp.validator import validate_name
from django import forms


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(), validators=[validate_name])
    image = forms.ImageField(widget=forms.FileInput(), required=False)
    age = forms.IntegerField(widget=forms.NumberInput(), required=False)

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'image', 'age')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = True
        self.fields['email'].widget.attrs['readonly'] = True
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise ValidationError('Вы слишком молоды!')
        return data

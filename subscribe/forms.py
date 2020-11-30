from django import forms
from .models import Signup


class SignupForm(forms.ModelForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={
        "type": "email",
        "name": "email",
        "id": "email",
        "placeholder": "Email Address",
        "class": "form-control sub-email",
        "autocomplete": "off",
        "required": "required",
    }))

    class Meta:
        model = Signup
        fields = ('email', )

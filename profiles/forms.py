from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea(attrs={
        "id": "bio_text_area",
        "rows": "3",
        'placeholder': 'Please enter your bio here ... '
    }))

    class Meta:
        model = Profile
        exclude = ('user',)

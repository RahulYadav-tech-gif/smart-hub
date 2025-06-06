from django import forms
from .models import UserProfile

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'middle_name', 'dob', 'phone', 'country', 'address',
            'gender', 'avatar', 'city', 'interests'
        ]

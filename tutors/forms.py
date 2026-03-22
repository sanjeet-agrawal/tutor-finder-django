from django import forms
from .models import Tutor

class TutorForm(forms.ModelForm):

    class Meta:
        model = Tutor
        fields = [
            'subject',
            'experience',
            'location',
            'hourly_rate',
            'bio',
            'photo'
        ]
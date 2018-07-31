from django import forms
from .models import User, Profile

class ProfileForm(forms.ModelForm):

  class Meta:
    model = Profile
    fields = ('dob', 'hometown', 'bio', 'image')

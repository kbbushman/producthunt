from django import forms
from .models import User, Profile

class ProfileForm(forms.ModelForm):

  class Meta:
    model = Profile
    fields = ('first_name', 'last_name', 'email','image', 'dob', 'hometown', 'bio')

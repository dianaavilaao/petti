from django.contrib.auth.forms import UserCreationForm
from pettiApp import models

class SignupForm(UserCreationForm):
    class Meta:
        model = models.User
        fields = [
            'email',
            'first_name',
            'last_name'
        ]

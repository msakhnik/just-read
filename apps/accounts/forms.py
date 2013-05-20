from  django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from apps.accounts.models import UserProfile

class RegisterForm(UserCreationForm):
    gender = forms.ChoiceField(choices = UserProfile.GENDER)
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, *args, **kwargs):

        user = super(RegisterForm, self).save(*args, **kwargs)
        user.email = self.cleaned_data["email"]

        UserProfile.objects.create(user = user, gender = self.cleaned_data['gender'])        

        return user
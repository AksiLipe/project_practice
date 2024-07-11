from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.forms import models


class ReceivingAnswerForm(forms.Form):
    user_answer = forms.CharField(label="Enter the Symbol:", max_length=1)


class SendingAnswerForm(forms.Form):
    user_answer = forms.CharField(label="Enter the Symbol:", max_length=10)

    def clean_user_answer(self):
        data = self.cleaned_data['user_answer']

        if len(data) > 10:
            raise ValidationError(
                'Maximum length of 10 symbols exceeded.'
            )

        if not all(char in [".", "-"] for char in data):
            raise ValidationError(
                'Invalid symbol. Please enter only "." or "-".'
            )

        return data


class UserForm(models.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

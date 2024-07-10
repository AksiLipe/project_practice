from django import forms
from django.core.exceptions import ValidationError


class ReceivingAnswerForm(forms.Form):
    user_answer = forms.CharField(label="Enter the Symbol:", max_length=1)


class SendingAnswerForm(forms.Form):
    user_answer = forms.CharField(label="Enter the Symbol:", max_length=10)

    def clean_user_answer(self):
        data = self.cleaned_data['user_answer']
        if data not in [".", "-"]:
            raise ValidationError(
                'Invalid symbol. Please enter only "." or "-".'
            )
        return data

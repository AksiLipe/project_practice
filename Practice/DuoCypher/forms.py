from django import forms


class AnswerForm(forms.Form):
    user_answer = forms.CharField(label="Enter the Symbol:", max_length=1)

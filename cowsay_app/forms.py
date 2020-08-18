from django import forms


class result(forms.Form):
    input_text = forms.CharField(max_length=30)

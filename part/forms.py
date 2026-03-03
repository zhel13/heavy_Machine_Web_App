from django import forms

class SearchPartForm(forms.Form):
    query = forms.CharField(
        label='',
        required=False,
        max_length=100,

        #TODO: add widget
    )
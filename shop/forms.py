''' Forms for shop app '''
from django import forms

class SearchForm(forms.Form):
    ''' Form for searching products '''
    query = forms.CharField()
    
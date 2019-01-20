from django import forms
from django.core import validators
from .core import Core


class initial_form(forms.Form):
    initials = forms.CharField(label='Your initials: ', max_length=3,
                               widget=forms.TextInput(attrs={
                                   'oninput': 'this.value = this.value.toUpperCase()',
                                   'pattern': '^[A-Z]+$',
                                   'autocomplete': 'off',
                               })
                               )
    font = forms.ChoiceField(label='Font: ', choices=Core().get_fonts().items())

    # TODO: get server-side validation working
    # validators = [validators.RegexValidator('^[A-Z]+$')]

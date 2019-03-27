from django import forms
from .models import Messages

class ContactForm(forms.ModelForm):

    class Meta():
        model = Messages

        fields = ('name', 'email', 'subject', 'message')
        widgets = {
            'name':forms.TextInput(attrs={
                'class': 'form-group col-lg-6 form-control',
                'placeholder':'Your Name'
            }),

            'email':forms.EmailInput(attrs={
                'class': 'form-group col-lg-6 form-control',
                'placeholder':'Your Email'
            }),

            'subject':forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Subject'
            }),

            'message': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Message'
            })

        }

        labels = {
            'name': '',
            'email': '',
            'subject': '',
            'message': ''
        }

from django.forms import ModelForm, TextInput, Textarea
from .models import ContactFormData


class ContactForm(ModelForm):
    class Meta:
        model = ContactFormData
        fields = '__all__'
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'email': TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'mobile': TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'message': Textarea(attrs={'class': 'form-control', 'required': 'required'}),
        }
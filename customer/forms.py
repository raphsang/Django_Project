from django import forms
from django.contrib.auth.models import User
from . import models
from django.forms import ModelForm, TextInput, EmailInput, NumberInput, DateInput
from .models import ClaimForm


class CustomerUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = ['username', 'address', 'mobile', 'national_id', 'profile_pic']


class ClaimFormForm(ModelForm):
    class Meta:
        model = ClaimForm
        fields = ['first_name', 'second_name', 'email', 'purchase_date', 'policy_type', 'claim_details', 'amount']
        widgets = {
            'first_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'First Name'
            }),
            'second_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Second Name'
            }),
            'email': EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 600px;',
                'placeholder': 'Email',
                'label': 'Email Address'
            }),
            'purchase_date': DateInput(attrs={
                'class': "form-control",
                'style': 'max-width: 600px;',
                'placeholder': 'Purchase Date (dd-mm-yy)'
            }),
            'policy_type': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 600px;',
                'placeholder': 'Policy Type'
            }),
            'amount': NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 600px;',
                'name': "age",
                'placeholder': 'Amount in Ksh'
            })
        }

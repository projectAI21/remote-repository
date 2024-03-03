from django import forms
from .models import Customer_details
from django.forms import BaseFormSet
from django.forms import modelformset_factory

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer_details
        exclude = ['s_no'] 




CustomerFormSet = modelformset_factory(Customer_details, form=CustomerForm, fields=('customer_name', 'customer_id', 'passport_id'), extra=0)


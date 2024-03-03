from django.shortcuts import render, redirect
from .forms import CustomerForm
from django.shortcuts import render, redirect
from .forms import CustomerForm  
from .forms import CustomerFormSet
from .models import *
from django.forms import modelformset_factory




def add_customer(request):
    customer_exists = False  # Initialize the variable
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer_id = form.cleaned_data['customer_id']
            passport_id = form.cleaned_data['passport_id']
            
            # Check if customer with given customer_id or passport_id already exists
            if Customer_details.objects.filter(customer_id=customer_id).exists() or \
               Customer_details.objects.filter(passport_id=passport_id).exists():
                # Customer already exists, set the variable to True
                customer_exists = True
            else:
                # Customer doesn't exist, save the form data
                form.save()
                return redirect('success_page')
    else:
        form = CustomerForm()
    
    return render(request, 'home.html', {'form': form, 'customer_exists': customer_exists})

def success_page(request):
    return render(request, 'success.html')


def customer_details(request):
    customers = Customer_details.objects.all()
    context = {
        'customers': customers,
    }
    
    return render(request, 'customer_details.html', context)


CustomerFormSet = modelformset_factory(Customer_details, form=CustomerForm, fields=('customer_name', 'customer_id', 'passport_id'), extra=0)

def edit_details(request):
    CustomerFormSet = modelformset_factory(Customer_details, form=CustomerForm, fields=('customer_name', 'customer_id', 'passport_id'), extra=0)

    if request.method == 'POST':
        formset = CustomerFormSet(request.POST)
        if formset.is_valid():
            instances = formset.save()
            return redirect('edit_details')
        else:
            print("Formset is not valid:", formset.errors)
    else:
        customers = Customer_details.objects.all()
        formset = CustomerFormSet(queryset=customers)

    return render(request, 'edit_details.html', {'formset': formset})



# Create your views here.

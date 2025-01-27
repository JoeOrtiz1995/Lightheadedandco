from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
  class Meta:
    model = Order
    fields = ('full_name', 'email', 'phone_number',
              'street_address1', 'town_or_city', 
              'postcode', 'county', 'country',)
  
  def __init__(self, *args, **kwargs):
    """
    Adds placeholders and classes, removes auto-generated
    labels and sets the autofocus on the full_name field
    """
    super().__init__(*args, **kwargs)
    placeholders = {
        'full_name': 'Full Name',
        'email': 'Email Address',
        'phone_number': 'Phone Number',
        'street_address1': 'Street Address 1',
        'town_or_city': 'Town or City',
        'postcode': 'Post Code',
        'county': 'County or State',
    }

    self.fields['full_name'].widget.attrs['autofocus'] = True
    for field in self.fields:
        if field != 'country':
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
        self.fields[field].label = False
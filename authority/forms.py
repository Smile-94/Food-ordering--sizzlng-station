from django import forms


from authority.models import BookTable
from products.models import Order
from authority.models import ShippingCharge

class TableBookingForm(forms.ModelForm):
    occasion = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Occasion Name (i,e Birth Day, Dinner)'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your email'}))
    full_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    messages =  messages = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter message'}))
    party_size = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Your party size (max-20)'}),max_value=20,)

    class Meta:
        model = BookTable
        exclude = ('table_no','review_message','is_active')

class TableBookingConfirmForm(forms.ModelForm):
    

    class Meta:
        model = BookTable
        fields = ('table_no','review_message',)

class ShippingChargeForm(forms.ModelForm):

    class Meta:
        model = ShippingCharge
        fields = ('shipping_charge',)
       
class ConfirmDeleveryForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('delevery_status',)
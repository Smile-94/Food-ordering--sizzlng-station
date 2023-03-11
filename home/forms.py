from django import forms

# models
from home.models import CustomerMessage


class CustomerMessageForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter Your Name'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Enter Your Email'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Write your message here'})
    )

    class Meta:
        model = CustomerMessage
        fields = ('name','email','message')
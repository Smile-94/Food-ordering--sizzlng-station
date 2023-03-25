from django import forms

# Models
from authority.models import FoodCategories
from authority.models import SetMenuFood
from authority.models import SetMenu
from authority.models import BookTable

# Widgets
from authority.widgets import CustomPictureImageFieldWidget

class FoodCategoriesForm(forms.ModelForm):
    photo = forms.ImageField(widget=CustomPictureImageFieldWidget)
    class Meta:
        model = FoodCategories
        fields = ('category_name', 'photo', 'sort_description')

class SetMenuFoodForm(forms.ModelForm):
    photo = forms.ImageField(widget=CustomPictureImageFieldWidget)
    class Meta:
        model = SetMenuFood
        fields = ('food_name','photo','description')

class SetMenuForm(forms.ModelForm):
    menu_image = forms.ImageField(widget=CustomPictureImageFieldWidget)
    class Meta:
        model = SetMenu
        exclude = ('menu_id','new_price','is_active')

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
        exclude = ('table_no','review_message')

class TableBookingConfirmForm(forms.ModelForm):

    class Meta:
        model = BookTable
        fields = ('table_no','review_message')
       


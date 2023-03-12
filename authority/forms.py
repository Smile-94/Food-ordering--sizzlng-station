from django import forms

# Models
from authority.models import FoodCategories
from authority.models import SetMenuFood
from authority.models import SetMenu

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
       


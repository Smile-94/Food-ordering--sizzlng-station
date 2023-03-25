from django import forms

from products.models import FoodCategories
from products.models import MenuFood
from products.models import Foods
# Widgets
from products.widgets import CustomPictureImageFieldWidget

class FoodCategoriesForm(forms.ModelForm):
    photo = forms.ImageField(widget=CustomPictureImageFieldWidget)
    class Meta:
        model = FoodCategories
        fields = ('category_name', 'photo', 'sort_description')

class MenuFoodForm(forms.ModelForm):
    photo = forms.ImageField(widget=CustomPictureImageFieldWidget)
    class Meta:
        model = MenuFood
        fields = ('food_name','photo','description')

class FoodsForm(forms.ModelForm):
    menu_image = forms.ImageField(widget=CustomPictureImageFieldWidget)
    class Meta:
        model = Foods
        exclude = ('menu_id','new_price','is_active')
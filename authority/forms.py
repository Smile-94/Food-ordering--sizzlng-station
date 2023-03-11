from django import forms




# Models
from authority.models import FoodCategories
from authority.models import SetMenuFood
from authority.models import SetMenu


class FoodCategoriesForm(forms.ModelForm):
    class Meta:
        model = FoodCategories
        fields = ('category_name', 'photo', 'sort_description')

class SetMenuFoodForm(forms.ModelForm):
    class Meta:
        model = SetMenuFood
        fields = ('food_name','photo','description')
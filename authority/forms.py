from django import forms

# Models
from authority.models import FoodCategories


class FoodCategoriesForm(forms.ModelForm):

    class Meta:
        model = FoodCategories
        fields = ('category_name', 'photo', 'sort_description')
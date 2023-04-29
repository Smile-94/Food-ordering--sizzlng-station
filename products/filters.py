

import django_filters
from django import forms

from products.models import Foods
from products.models import FoodCategories
from products.models import Order

class FoodsFilter(django_filters.FilterSet):
    menu_name = django_filters.CharFilter(field_name='menu_name', lookup_expr='icontains')
    food_catagory = django_filters.ModelChoiceFilter(queryset=FoodCategories.objects.all())

    class Meta:
        model = Foods
        fields = ['menu_name', 'food_catagory']

class OrderFilter(django_filters.FilterSet):
    from_date = django_filters.DateFilter(field_name='ordered_at', lookup_expr='gte', widget=forms.DateInput(attrs={'type': 'date'}), label='From')
    to_date = django_filters.DateFilter(field_name='ordered_at', lookup_expr='lte', widget=forms.DateInput(attrs={'type': 'date'}), label='To')

    class Meta:
        model = Order
        fields = ['ordered_at']

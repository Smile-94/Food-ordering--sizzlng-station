
import django_filters
from django import forms

from authority.models import BookTable



class TableFilter(django_filters.FilterSet):
    from_date = django_filters.DateFilter(field_name='date', lookup_expr='gte', widget=forms.DateInput(attrs={'type': 'date'}), label='From')
    to_date = django_filters.DateFilter(field_name='date', lookup_expr='lte', widget=forms.DateInput(attrs={'type': 'date'}), label='To')

    class Meta:
        model = BookTable
        fields = ['date']
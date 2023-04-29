from django_filters.views import FilterView

# Generic Classes
from django.views.generic import DetailView


# Models
from products.models import Foods

from products.filters import FoodsFilter


class SetMenuDetailsView(DetailView):
    model = Foods
    context_object_name = 'setmenu'
    template_name = 'home/set_menu_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Set Menu Details"
        context["setmenus"] = Foods.objects.filter(is_active = True).order_by('-id')[0:7]
        return context

class FoodsSearchView(FilterView):
    model = Foods
    filterset_class = FoodsFilter
    context_object_name = 'all_foods'
    template_name = 'home/search_foods.html'

    def get_queryset(self):
        qs = super().get_queryset()
        search_term = self.request.GET.get('s')
        if search_term:
            qs = qs.filter(menu_name__icontains=search_term)
        return qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Search Product"
        return context
    
    
from django.urls import reverse_lazy

# Generic Classes
from django.views.generic import CreateView

# Permission Classes
from django.contrib.auth.mixins import LoginRequiredMixin
from authority.permissions import AdminPassesTestMixin

# Models 
from authority.models import FoodCategories

# Forms
from authority.forms import FoodCategoriesForm

class AddFoodCategoryView(LoginRequiredMixin, AdminPassesTestMixin, CreateView):
    model = FoodCategories
    form_class = FoodCategoriesForm
    queryset = FoodCategories.objects.filter(is_active=True)
    template_name = 'authority/food_categories.html'
    success_url = reverse_lazy('authority:add_food_category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Food Catagories" 
        context["categories"] = self.queryset
        return context
    
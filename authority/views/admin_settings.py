from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect

# Generic Classes
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

# Permission Classes
from django.contrib.auth.mixins import LoginRequiredMixin
from authority.permissions import AdminPassesTestMixin

# Models 
from products.models import FoodCategories
from authority.models import ShippingCharge

# Forms
from products.forms import FoodCategoriesForm
from authority.forms import ShippingChargeForm

class AddFoodCategoryView(LoginRequiredMixin, AdminPassesTestMixin, CreateView):
    model = FoodCategories
    form_class = FoodCategoriesForm
    template_name = 'authority/food_categories.html'
    success_url = reverse_lazy('authority:add_food_category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Food Catagories" 
        context["categories"] = FoodCategories.objects.filter(is_active=True)
        return context
    
    def form_valid(self, form):
        cagegory_name=form.cleaned_data.get('category_name')
        messages.success(self.request, f"Category {cagegory_name} added successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error("Something went worng try again!")
        return super().form_invalid(form)
    
class UpdateFoodCategoryView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model = FoodCategories
    form_class = FoodCategoriesForm
    template_name = 'authority/food_categories.html'
    success_url = reverse_lazy('authority:add_food_category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Food Catagories" 
        context["updated"] = True
        return context
    
    def form_valid(self, form):
        cagegory_name=form.cleaned_data.get('category_name')
        messages.success(self.request, f"Category {cagegory_name} updated successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error("Something went worng try again!")
        return super().form_invalid(form)

class DeleteFoodCategoryView(LoginRequiredMixin, AdminPassesTestMixin, DeleteView):
    model= FoodCategories
    context_object_name = 'category'
    template_name = "authority/delete_food_category.html"
    success_url = reverse_lazy('authority:add_food_category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Food Category" 
        return context

    def form_valid(self, form):
        self.object.is_active = False
        self.object.save()
        return redirect(self.success_url) 


class AddShippingChargeView(LoginRequiredMixin, AdminPassesTestMixin, CreateView):
    model = ShippingCharge
    form_class = ShippingChargeForm
    template_name = 'authority/shipping_charge.html'
    success_url = reverse_lazy('authority:add_shipping_charge')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Shipping Charge" 
        context["shippings"] = ShippingCharge.objects.all()
        return context
    
    def form_valid(self, form):
        messages.success(self.request, f"Shipping charge added successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error("Something went worng try again!")
        return super().form_invalid(form)

class UpdateShippingChargeView(LoginRequiredMixin,AdminPassesTestMixin, UpdateView):
    model = ShippingCharge
    form_class = ShippingChargeForm
    template_name = 'authority/shipping_charge.html'
    success_url = reverse_lazy('authority:add_shipping_charge')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Shipping Charge" 
        context["updated"] = True
        return context
    
    def form_valid(self, form):
        cagegory_name=form.cleaned_data.get('category_name')
        messages.success(self.request, f"Shipping Charge updated successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error("Something went worng try again!")
        return super().form_invalid(form)
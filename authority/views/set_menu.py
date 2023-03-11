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
from authority.models import SetMenuFood

# Forms
from authority.forms import SetMenuFoodForm


class AddSetMenuFoodView(LoginRequiredMixin, AdminPassesTestMixin, CreateView):
    model = SetMenuFood
    form_class = SetMenuFoodForm
    template_name = 'authority/add_set_menu_food.html'
    success_url = reverse_lazy('authority:add_set_menu_food')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Food Catagories" 
        context["foods"] = SetMenuFood.objects.filter(is_active=True)
        return context
    
    def form_valid(self, form):
        cagegory_name=form.cleaned_data.get('category_name')
        messages.success(self.request, f"Category {cagegory_name} added successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error("Something went worng try again!")
        return super().form_invalid(form)
    
class UpdateSetMenuFoodView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model = SetMenuFood
    form_class = SetMenuFoodForm
    template_name = 'authority/add_set_menu_food.html'
    success_url = reverse_lazy('authority:add_set_menu_food')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Food Catagories" 
        context["updated"] = True
        return context
    
    def form_valid(self, form):
        food_name=form.cleaned_data.get('food_name')
        messages.success(self.request, f"{food_name} updated successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error("Something went worng try again!")
        return super().form_invalid(form)

class DeleteFoodCategoryView(LoginRequiredMixin, AdminPassesTestMixin, DeleteView):
    model= SetMenuFood
    context_object_name = 'foods'
    template_name = "authority/delete_set_menu_food.html"
    success_url = reverse_lazy('authority:add_set_menu_food')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Food" 
        return context

    def form_valid(self, form):
        self.object.is_active = False
        self.object.save()
        return redirect(self.success_url) 
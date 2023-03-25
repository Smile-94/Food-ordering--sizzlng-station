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
from products.models import MenuFood
from products.models import Foods

# Forms
from products.forms import MenuFoodForm
from products.forms import FoodsForm


class AddMenuFoodView(LoginRequiredMixin, AdminPassesTestMixin, CreateView):
    model = MenuFood
    form_class = MenuFoodForm
    template_name = 'authority/add_set_menu_food.html'
    success_url = reverse_lazy('authority:add_set_menu_food')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Food Catagories" 
        context["foods"] = MenuFood.objects.filter(is_active=True)
        return context
    
    def form_valid(self, form):
        food_name=form.cleaned_data.get('food_name')
        messages.success(self.request, f"{food_name} added successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Something went worng try again!")
        return super().form_invalid(form)
    
class UpdateMenuFoodView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model = MenuFood
    form_class = MenuFoodForm
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
        messages.error(self.request, "Something went worng try again!")
        return super().form_invalid(form)

class DeleteMenuFoodView(LoginRequiredMixin, AdminPassesTestMixin, DeleteView):
    model= MenuFood
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


class AddFoodsView(LoginRequiredMixin, AdminPassesTestMixin, CreateView):
    model = Foods
    form_class = FoodsForm
    template_name = 'authority/add_set_menu.html'
    success_url = reverse_lazy('authority:add_set_menu')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Set Menu" 
        context["setmenus"] = Foods.objects.filter(is_active=True)
        return context
    
    def form_valid(self, form):
        menu_name=form.cleaned_data.get('menu_name')
        messages.success(self.request, f"{menu_name} added successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Something went worng try again!")
        return super().form_invalid(form)

class UpdateFoodsView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model = Foods
    form_class = FoodsForm
    template_name = 'authority/add_set_menu.html'
    success_url = reverse_lazy('authority:add_set_menu')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Set Menu" 
        context["updated"] = True
        return context
    
    def form_valid(self, form):
        menu_name=form.cleaned_data.get('menu_name')
        messages.success(self.request, f"{menu_name} updated successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Something went worng try again!")
        return super().form_invalid(form)


class DeleteFoodsView(LoginRequiredMixin, AdminPassesTestMixin, DeleteView):
    model= Foods
    context_object_name = 'menus'
    template_name = "authority/delete_set_menu.html"
    success_url = reverse_lazy('authority:add_set_menu')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Food" 
        return context

    def form_valid(self, form):
        self.object.is_active = False
        self.object.save()
        return redirect(self.success_url) 
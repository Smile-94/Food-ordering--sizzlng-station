from django.shortcuts import render

# Generic Classes
from django.views.generic import TemplateView

# Forms
from home.forms import CustomerMessageForm
from authority.models import FoodCategories

# Create your views here.
class IndexView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home" 
        context["categories"] =FoodCategories.objects.filter(is_active=True)

        return context

class ContactView(TemplateView):
    template_name = 'home/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Contact With Us'
        context["form"] = CustomerMessageForm
        return context

    
    


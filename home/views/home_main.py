from django.shortcuts import render

# Generic Classes
from django.views.generic import TemplateView

# Forms
from home.forms import CustomerMessageForm
from authority.models import SetMenu

# Create your views here.
class IndexView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home" 
        context["setmenus"] = SetMenu.objects.filter(is_active=True).order_by('-id')[:8]
        return context

class ContactView(TemplateView):
    template_name = 'home/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Contact With Us'
        context["form"] = CustomerMessageForm
        return context


class ContactUsView(TemplateView):
    
    template_name = 'home/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Contact Us"
        return context
    

    
    


from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages

# Generic Classes
from django.views.generic import TemplateView
from django.views.generic import CreateView

# Forms
from home.forms import CustomerMessageForm
from authority.forms import TableBookingForm

#Models
from authority.models import BookTable
from products.models import Foods

# Create your views here.
class IndexView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home" 
        context["setmenus"] = Foods.objects.filter(is_active=True).order_by('-id')[:8]
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
    
class TableBookingView(CreateView):
    model = BookTable
    form_class = TableBookingForm
    template_name = 'home/table_booking.html'
    success_url = reverse_lazy('home:table_booking')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Table Booking' 
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "We will get back to you soon")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Some thing wrong try agian!")
        return super().form_invalid(form)

class ShopeView(TemplateView):
    template_name = 'home/shope.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Shope Page"
        context["recent_product"] = Foods.objects.filter(is_active=True).order_by('-id')[:8]
        context["all_foods"] = Foods.objects.filter(is_active=True).order_by('-id')
        return context
    
    
    


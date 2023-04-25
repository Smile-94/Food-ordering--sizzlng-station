

# Generic Classes
from django.views.generic import TemplateView

# Permission Classes
from django.contrib.auth.mixins import LoginRequiredMixin
from authority.permissions import AdminPassesTestMixin

# models
from home.models import CustomerMessage
from products.models import Order
from authority.models import ShippingCharge



class AdminHomeView(LoginRequiredMixin, AdminPassesTestMixin, TemplateView):
    template_name = 'authority/admin.html'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset =CustomerMessage.objects.filter(is_active=True)
        context["title"] = "Admin Home"
        context["custormermessages"] = queryset.order_by('-id')[:5]
        context["orders"] = Order.objects.filter(ordered=True, order_confirm=False).order_by('-id')[0:10]
        context["shipping_charge"] = ShippingCharge.objects.latest('id')
        return context
    
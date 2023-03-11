

# Generic Classes
from django.views.generic import TemplateView

# Permission Classes
from django.contrib.auth.mixins import LoginRequiredMixin
from authority.permissions import AdminPassesTestMixin

# models
from home.models import CustomerMessage



class AdminHomeView(LoginRequiredMixin, AdminPassesTestMixin, TemplateView):
    template_name = 'authority/admin.html'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset =CustomerMessage.objects.filter(is_active=True)
        context["title"] = "Admin Home"
        context["messages"] = queryset.order_by('-id')[:5]
        return context
    
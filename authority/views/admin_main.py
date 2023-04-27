from django.utils import timezone
from django.db.models import Q

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
        today = timezone.now().date()
        orders_today = Order.objects.filter(Q(confirmed_at__year=today.year) & Q(confirmed_at__month=today.month) & Q(confirmed_at__day=today.day) & Q(ordered=True, order_confirm= True))
        orders_all = Order.objects.filter(Q(ordered=True, order_confirm= True))

        total_orders_today = orders_today.count()
        all_orders = orders_all.count()

        total_sales = 0
        for order in orders_today:
            total_sales += order.get_totals()
        
        all_total_salse = 0
        for order in  orders_all:
            all_total_salse += order.get_totals()

        context = super().get_context_data(**kwargs)
        queryset =CustomerMessage.objects.filter(is_active=True)
        context["title"] = "Admin Home"
        context["custormermessages"] = queryset.order_by('-id')[:5]
        context["orders"] = Order.objects.filter(ordered=True, order_confirm=False).order_by('-id')[0:10]
        context["shipping_charge"] = ShippingCharge.objects.latest('id')
        context["total_sales"] = total_sales
        context["all_total_salse"] = all_total_salse
        context["total_orders_today"] = total_orders_today
        context["all_orders"] = all_orders
        return context
    
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect

# Permission Classes
from django.contrib.auth.mixins import LoginRequiredMixin
from authority.permissions import AdminPassesTestMixin

# Generic Classes
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView


# Models 
from products.models import Order
from authority.models import ShippingCharge

# Forms
from authority.forms import TableBookingConfirmForm



class PendingListView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    model = Order
    queryset = Order.objects.filter(ordered=True, order_confirm=False).order_by('-id')
    context_object_name = 'orders'
    template_name = 'authority/order_details.html'

    def get_context_data(self, **kwargs):
        print('Query Set: ',self.queryset)
        context = super().get_context_data(**kwargs)
        context["title"] = "Pending Order List" 
        return context

class ConfirmedOrderListView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    model = Order
    queryset = Order.objects.filter(ordered=True, order_confirm=False).order_by('-id')
    context_object_name = 'orders'
    template_name = 'authority/order_details.html'

    def get_context_data(self, **kwargs):
        print('Query Set: ',self.queryset)
        context = super().get_context_data(**kwargs)
        context["title"] = "Confirmed Order List" 
        return context


class OrderDetailsView(LoginRequiredMixin, AdminPassesTestMixin, DetailView):
    model = Order
    context_object_name = 'order'
    template_name = 'authority/order_details.html'

    def get_context_data(self, **kwargs):
        shipping_charge = ShippingCharge.objects.latest('id')
        order_total = Order.objects.filter(id=self.kwargs['pk'])[0]
        context = super().get_context_data(**kwargs)
        context["title"] = 'Order Details' 
        context["details"] = True
        context["shipping_charge"] = shipping_charge
        context["total"] = order_total.get_totals()+shipping_charge.shipping_charge
        context["form"] = TableBookingConfirmForm(instance=self.object)
        return context

class ConfirmOrderView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model = Order
    form_class = TableBookingConfirmForm
    template_name = 'authority/booking_request_list.html'
    success_url = reverse_lazy('authority:table_bookig_details', kwargs={'pk': 0})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Confirm Table Booking Request"
        return context
    
    def form_valid(self, form):
        booking_message = form.cleaned_data.get('review_message')
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.confirm_status = True
            form_obj.save()
            # Send Mail
        subject = 'Table Booking Confirmation Mail'
        message = booking_message
        from_email = 'vsmpsm2023@gmail.com'
        recipient_list = [ 'mshossen75@gmail.com',]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        messages.success(self.request, "Appointment Accept Successfully")
        self.success_url = reverse_lazy('authority:table_bookig_details', kwargs={'pk': self.object.id})
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Something wrong try again!")
        return super().form_invalid(form)


class DelteBookTableView(LoginRequiredMixin, AdminPassesTestMixin, DeleteView):
    model= Order
    context_object_name ='booktable'
    template_name = "authority/booking_request_list.html"
    success_url = reverse_lazy('authority:table_bookig_request_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Booking Table" 
        context["deleted"] = True
        return context

    def form_valid(self, form):
        self.object.is_active = False
        self.object.save()
        return redirect(self.success_url)

from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Models
from payment.models import BillingAddress
from products.models import Order
from products.models import Cart

# Forms
from payment.forms import BillingAddressForm

# Create your views here.
@login_required
def check_out(request):
    saved_address = BillingAddress.objects.get_or_create(user = request.user)[0]
    form = BillingAddressForm(instance=saved_address)
    if request.method == 'POST':
        form = BillingAddressForm(request.POST, instance=saved_address)
        if form.is_valid():
            form.user = request.user 
            form.save()
            form = BillingAddressForm(instance=saved_address)
    
    order_qs = Order.objects.filter(user=request.user, ordered = False)
    order_items = order_qs[0].orderitems.all()
    total_item = order_qs[0].orderitems.all().count()
    order_total = order_qs[0].get_totals()
           


    return render(request, 'payment/check_out.html', context={'form':form, 'order_items':order_items,'order_total':order_total, 'total_item':total_item})


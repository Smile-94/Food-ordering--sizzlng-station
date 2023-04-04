from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.db.models import F, Sum

# Generic Classes
from django.views.generic import TemplateView

# Permission 

# Models
from products.models import Cart
from products.models import Order
from products.models import Foods
from accounts.models import User


@login_required
def add_to_cart(request, pk):
    item = get_object_or_404(Foods, id=pk)

    order_item = Cart.objects.get_or_create(items=item, user=request.user,purchased=False)
    order_qs = Order.objects.filter(user = request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        
        if order.orderitems.filter(items=item).exists():
            order_item[0].quentity +=1
            order_item[0].save()
            return redirect('home:index')
        else:
            order.orderitems.add(order_item[0])
            return redirect('home:index')
    else:
        order = Order(user=request.user)
        order.save()
        order.orderitems.add(order_item[0])
        return redirect('home:index')

class ChartProductListView(TemplateView):

    template_name = 'home/cart_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Cart Page"
        context["foods"] = Foods.objects.filter(is_active=True).order_by('-id')[:10]
        context["chart_items"] = Cart.objects.filter(user =self.request.user, purchased = False)
        context["total_items"] = Cart.objects.filter(user =self.request.user, purchased = False).count()
        context["total_price"] =Cart.objects.filter(user=self.request.user, purchased=False).annotate(item_total=F('quentity') * F('items__new_price')).aggregate(total_price=Sum('item_total'))['total_price'] or 0
        return context

@login_required
def remove_form_cart(request, pk):
    item = get_object_or_404(Foods, id = pk)
    order_qs = Order.objects.filter(user = request.user, ordered = False)

    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(items=item).exists():
            order_item = Cart.objects.filter(items=item, user= request.user, purchased=False )[0]
            order.orderitems.remove(order_item)
            order_item.delete()
            return redirect('home:cart_details')
        else:
            return redirect('home:index')
    else:
        return redirect('home:index')

@login_required
def increase_cart_item(request, pk):
    item = get_object_or_404(Foods, id = pk)
    order_qs = Order.objects.filter(user = request.user, ordered = False)

    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(items=item).exists():
            order_item = Cart.objects.filter(items=item, user= request.user, purchased=False )[0]

            if order_item.quentity >= 1:
                order_item.quentity +=1
                order_item.save()
            return redirect('home:cart_details')
        else:
            return redirect('home:index')
    else:
        return redirect('home:index')
    
@login_required
def decrease_cart_item(request, pk):
    item = get_object_or_404(Foods, id = pk)
    order_qs = Order.objects.filter(user = request.user, ordered = False)

    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(items=item).exists():
            order_item = Cart.objects.filter(items=item, user= request.user, purchased=False )[0]

            if order_item.quentity > 1:
                order_item.quentity -=1
                order_item.save()
                return redirect('home:cart_details')
            else:
                order.orderitems.remove(order_item)
                order_item.delete()
                return redirect('home:cart_details')
        else:
            return redirect('home:index')
    else:
        return redirect('home:index')

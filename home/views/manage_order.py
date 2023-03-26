from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.db.models import F


# Permission 

# Models
from products.models import Cart
from products.models import Foods
from accounts.models import User


class AddToCartView():
    from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from products.models import Cart, Foods

class AddToCartView(CreateView):
    model = Cart
    fields = ['quentity']
    template_name ='home/add_to_cart.html'
    success_url = reverse_lazy('home:index')  # the URL to redirect to after adding to cart

    def form_valid(self, form):
        # get the food item and user from the URL parameters
        food_id = self.kwargs['pk']
        user_id = self.request.user.id

        # get the food item object and user object from the database
        food = get_object_or_404(Foods, id=food_id)
        user = get_object_or_404(User, id=user_id)

        # check if the item already exists in the user's cart
        cart_item = Cart.objects.filter(items=food, user=user, purchased=False).first()
        if cart_item:
            Cart.objects.filter(pk=cart_item.pk).update(quentity=F('quentity') + form.cleaned_data['quentity'])
        else:
            # if the item doesn't exist, add it to the cart
            cart_item = form.save(commit=False)
            cart_item.items = food  # set the items field
            cart_item.user = user
            cart_item.save()

        return super().form_valid(form)
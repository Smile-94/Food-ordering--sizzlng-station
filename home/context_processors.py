from products.models import FoodCategories
from products.models import Cart
from django.db.models import F, Sum

def my_context_processor(request):
    # your code here to get the data you want to pass to the base template
    food_category = FoodCategories.objects.filter(is_active=True)
    chart_items = Cart.objects.filter(user = request.user, purchased = False)
    chart_item_quetity = Cart.objects.filter(user = request.user, purchased = False).count()
    total_price = Cart.objects.filter(user=request.user, purchased=False).annotate(item_total=F('quentity') * F('items__new_price')).aggregate(total_price=Sum('item_total'))['total_price'] or 0
    total_price = "{:.2f}".format(float(total_price))
    return {
        "food_categories": food_category,
        'chart_items':chart_items,
        'chart_item_quetity':chart_item_quetity,
        'cart_price':total_price
        }
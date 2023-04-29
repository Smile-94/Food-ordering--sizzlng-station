from products.models import FoodCategories
from products.models import Cart
from django.db.models import F, Sum

from products.filters import FoodsFilter
from products.models import Foods

def my_context_processor(request):
    data_dic = {}
    # your code here to get the data you want to pass to the base template
    food_category = FoodCategories.objects.filter(is_active=True)
    data_dic.update({"food_categories": food_category,})
    try:

        chart_items = Cart.objects.filter(user = request.user, purchased = False)
        chart_item_quetity = Cart.objects.filter(user = request.user, purchased = False).count()
        total_price = Cart.objects.filter(user=request.user, purchased=False).annotate(item_total=F('quentity') * F('items__new_price')).aggregate(total_price=Sum('item_total'))['total_price'] or 0
        total_price = "{:.2f}".format(float(total_price))
        data_dic.update({
            'chart_items':chart_items,
            'chart_item_quetity':chart_item_quetity,
            'cart_price':total_price,
            'foods_filter': FoodsFilter(request.GET or None, queryset=Foods.objects.all())
        })
    except Exception as e:
        print(e)
    
    return data_dic
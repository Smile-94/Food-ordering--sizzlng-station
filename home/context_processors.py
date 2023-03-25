from products.models import FoodCategories

def my_context_processor(request):
    # your code here to get the data you want to pass to the base template
    food_category = FoodCategories.objects.filter(is_active=True)
    return {"food_categories": food_category}
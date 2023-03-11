from django.urls import path


app_name = 'authority'

# Views
from authority.views import admin_main
from authority.views import admin_settings

urlpatterns = [
    path('authority/', admin_main.AdminHomeView.as_view(), name='authority')
    
]

# manage admin settings
urlpatterns += [
    path('add-food-category/', admin_settings.AddFoodCategoryView.as_view(), name='add_food_category')
]

from django.urls import path


app_name = 'authority'

# Views
from authority.views import admin_main
from authority.views import admin_settings
from authority.views import set_menu

urlpatterns = [
    path('authority/', admin_main.AdminHomeView.as_view(), name='authority')
    
]

# manage set menu
urlpatterns += [
    path('add-set-menu-food/', set_menu.AddSetMenuFoodView.as_view(), name='add_set_menu_food'),
    path('update-set-menu-food/<int:pk>/', set_menu.UpdateSetMenuFoodView.as_view(), name='update_set_menu_food'),
    path('delete-set-menu-food/<int:pk>/', set_menu.DeleteFoodCategoryView.as_view(), name='delete_set_menu_food'),
    path('add-set-menu/', set_menu.AddSetMenuView.as_view(), name='add_set_menu'),
    path('update-set-menu/<int:pk>/', set_menu.UpdateSetMenuView.as_view(), name='update_set_menu'),
    path('delete-set-menu/<int:pk>/', set_menu.DeleteSetMenuView.as_view(), name='delete_set_menu'),
    
]


# manage admin settings
urlpatterns += [
    path('add-food-category/', admin_settings.AddFoodCategoryView.as_view(), name='add_food_category'),
    path('update-food-category/<int:pk>/', admin_settings.UpdateFoodCategoryView.as_view(), name='update_food_category'),
    path('delete-food-category/<int:pk>/', admin_settings.DeleteFoodCategoryView.as_view(), name='delete_food_category'),
]

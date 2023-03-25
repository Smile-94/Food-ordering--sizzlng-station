from django.urls import path


app_name = 'authority'

# Views
from authority.views import admin_main
from authority.views import manage_table
from authority.views import admin_settings
from authority.views import manage_foods

urlpatterns = [
    path('authority/', admin_main.AdminHomeView.as_view(), name='authority')
    
]

# manage set menu
urlpatterns += [
    path('add-set-menu-food/', manage_foods.AddMenuFoodView.as_view(), name='add_set_menu_food'),
    path('update-set-menu-food/<int:pk>/', manage_foods.UpdateMenuFoodView.as_view(), name='update_set_menu_food'),
    path('delete-set-menu-food/<int:pk>/', manage_foods.DeleteMenuFoodView.as_view(), name='delete_set_menu_food'),
    path('add-set-menu/', manage_foods.AddFoodsView.as_view(), name='add_set_menu'),
    path('update-set-menu/<int:pk>/', manage_foods.UpdateFoodsView.as_view(), name='update_set_menu'),
    path('delete-set-menu/<int:pk>/', manage_foods.DeleteFoodsView.as_view(), name='delete_set_menu'),
    
]

# Manage Table
urlpatterns += [
    path('table-booking-request/', manage_table.TableBookingRequestListView.as_view(), name='table_bookig_request_list'),
    path('table-booked-list/', manage_table.TableBookedListView.as_view(), name='table_booked_list'),
    path('table-booking-details/<int:pk>/', manage_table.TableBookingDetailsView.as_view(), name='table_bookig_details'),
    path('table-booking-confirm/<int:pk>/', manage_table.ConfirmTableBookingView.as_view(), name='table_bookig_confirm'),
    path('table-booking-delete/<int:pk>/', manage_table.DelteBookTableView.as_view(), name='table_bookig_delete'),
]


# manage admin settings
urlpatterns += [
    path('add-food-category/', admin_settings.AddFoodCategoryView.as_view(), name='add_food_category'),
    path('update-food-category/<int:pk>/', admin_settings.UpdateFoodCategoryView.as_view(), name='update_food_category'),
    path('delete-food-category/<int:pk>/', admin_settings.DeleteFoodCategoryView.as_view(), name='delete_food_category'),
]

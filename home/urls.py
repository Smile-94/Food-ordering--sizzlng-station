from django.urls import path

# Views
from home.views import home_main
from home.views import customer_message
from home.views import customer_login
from home.views import manage_product

app_name = 'home'

urlpatterns = [

    path('', home_main.IndexView.as_view(),name="index"),
    path('home/', home_main.IndexView.as_view(),name="home"),
    path('contact/', home_main.ContactView.as_view(),name="contact"),
    path('table-booking/', home_main.TableBookingView.as_view(),name="table_booking"),
    
]

urlpatterns += [
    path('customer-message/', customer_message.CustomerMessageView.as_view(), name='customer_message'),
]

# Manage customer login logout
urlpatterns += [
    path('customer-login/', customer_login.CustomerUserLoginView.as_view(),name="customer_login"),
    path('customer-logout/', customer_login.CustomerUserLogout.as_view(),name="customer_logout")
]

# Manage Product
urlpatterns += [
    path('set-menu-details/<int:pk>/', manage_product.SetMenuDetailsView.as_view(), name='set-menu-details')
]


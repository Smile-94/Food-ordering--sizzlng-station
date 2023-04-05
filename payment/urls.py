from django.urls import path

app_name = 'payment'

from payment.views import check_out

urlpatterns = [
    path('checkout/', check_out, name='checkout'),
]
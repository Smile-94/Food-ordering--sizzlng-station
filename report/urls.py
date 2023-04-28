from django.urls import path

from report.views import OrderPdfView

app_name = 'report'

urlpatterns = [
    path('order-pdf/<int:pk>/', OrderPdfView.as_view(), name='order_pdf'),
]
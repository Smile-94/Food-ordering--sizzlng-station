from django.shortcuts import render

# Create your views here.
# for generating pdf
from django.views.generic.detail import DetailView
from django_xhtml2pdf.views import PdfMixin
from django.conf import settings

# Models
from products.models import Order
from authority.models import ShippingCharge


class OrderPdfView(PdfMixin, DetailView):
    model = Order
    context_object_name = 'order'
    template_name = "report/order_pdf.html"

    def get_context_data(self, **kwargs):
        shipping_charge = ShippingCharge.objects.latest('id')
        order_total = Order.objects.filter(id=self.kwargs['pk'])[0]
        context = super().get_context_data(**kwargs)
        context['static_url'] = self.request.build_absolute_uri(settings.STATIC_URL)
        context['shipping_charge'] = shipping_charge
        context["total"] = order_total.get_totals()+shipping_charge.shipping_charge
        return context
    
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        response = self.render_to_response(context)
        filename = "profile_{0}.pdf".format(self.object.pk)
        response['Content-Disposition'] = 'filename="{}"'.format(filename)
        return response


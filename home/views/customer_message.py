from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.urls import reverse




# Generic Classes
from django.views.generic import CreateView

# models 
from home.models import CustomerMessage

# forms
from home.forms import CustomerMessageForm

class CustomerMessageView(CreateView):
    model = CustomerMessage
    form_class = CustomerMessageForm

    def form_valid(self, form):

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home:contact'))
        
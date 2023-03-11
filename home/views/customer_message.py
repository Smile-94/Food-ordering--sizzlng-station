from django.http import JsonResponse
# Generic Classes
from django.views.generic import CreateView

# models 
from home.models import CustomerMessage

# forms
from home.forms import CustomerMessageForm

class CustomerMessageView(CreateView):
    model = CustomerMessage
    form_class = CustomerMessageForm
    http_method_names = ['get', 'post']

    def form_valid(self, form):

        if form.is_valid():
            form.save()
            data={
                'ok':'ok'
            }
            return JsonResponse({'message': 'success', 'data': {'error_message': 'There was a problem processing your request.'}})
        else:
            return JsonResponse({'message': 'error', 'data': form.errors})
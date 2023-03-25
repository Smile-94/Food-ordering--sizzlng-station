

# Generic Classes
from django.views.generic import DetailView


# Models
from products.models import Foods


class SetMenuDetailsView(DetailView):
    model = Foods
    context_object_name = 'setmenu'
    template_name = 'home/set_menu_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Set Menu Details"
        context["setmenus"] = Foods.objects.filter(is_active = True).order_by('-id')[0:7]
        return context
    
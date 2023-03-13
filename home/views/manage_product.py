

# Generic Classes
from django.views.generic import DetailView


# Models
from authority.models import SetMenu


class SetMenuDetailsView(DetailView):
    model = SetMenu
    context_object_name = 'setmenu'
    template_name = 'home/set_menu_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Set Menu Details"
        context["setmenus"] = SetMenu.objects.filter(is_active = True).order_by('-id')[0:7]
        return context
    
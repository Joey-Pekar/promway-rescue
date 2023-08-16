from django.views import generic

from .models import Dog

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'dogs/index.html'
    context_object_name = "available_rescues"

    def get_queryset(self):
        return Dog.objects.filter(adopted=False).order_by("id")[:3]
    
class AdoptableView(generic.ListView):
    template_name = 'dogs/adoptable.html'
    context_object_name = "available_rescues"

    def get_queryset(self):
        return Dog.objects.filter(adopted=False).filter(hidden=False).order_by("name")

class DetailView(generic.DetailView):
    model = Dog
    template_name = 'dogs/details.html'
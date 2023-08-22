from typing import Any, Dict
from django.views import generic
from django.utils import timezone

from .models import Dog, Event

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'dogs/index.html'
    context_object_name = "available_rescues"

    def get_queryset(self):
        return Dog.objects.filter(adopted=False).order_by('?')[:3]
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(events = Event.objects.order_by("time").order_by("date").filter(date__gt=timezone.now()))
    
class AdoptableView(generic.ListView):
    template_name = 'dogs/adoptable.html'
    context_object_name = "available_rescues"

    def get_queryset(self):
        return Dog.objects.filter(adopted=False).filter(hidden=False).order_by("name")
    

class DetailView(generic.DetailView):
    model = Dog
    template_name = 'dogs/details.html'
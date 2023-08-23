from typing import Any, Dict
from django.views import generic
from django.utils import timezone
from django.shortcuts import render

from .models import Dog, Event

# Create your views here.

def Index(request):

    rescues = Dog.objects.filter(adopted=False).order_by('?')[:3]
    events = Event.objects.order_by("time").order_by("date").filter(date__gt=timezone.now())

    context = {
        "rescues": rescues, 
        "events": events
        }
    
    return render(request, "dogs/index.html", context)
    
class AdoptableView(generic.ListView):
    template_name = 'dogs/adoptable.html'
    context_object_name = "available_rescues"

    def get_queryset(self):
        return Dog.objects.filter(adopted=False).filter(hidden=False).order_by("name")
    

class DetailView(generic.DetailView):
    model = Dog
    template_name = 'dogs/details.html'
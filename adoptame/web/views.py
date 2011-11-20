from web.models import *
from django.shortcuts import render_to_response, RequestContext
from django.views.generic import ListView, DetailView

class HomeView(ListView):
    template_name = 'home.html'
    paginate_by = 20
    queryset = Animal.objects.all().order_by('-pub_date')[:20]


class AnimalView(DetailView):
    template_name = 'animal_detail.html'
    queryset = Animal.objects.all()

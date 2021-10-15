from django.views.generic import ListView, DeleteView
from .models import Cheese

class CheeseListView(ListView):
    model = Cheese
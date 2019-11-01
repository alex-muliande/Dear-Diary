from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from users.models import Profile
from entries.models import Entry
# from .forms import NeighbourhoodForm,BusinessForm,PostForm

# Create your views here.


def index(request):


    entries = Entry.objects.order_by('-date_posted')
    print('***')
    context = {
        'entries' : entries
    }
    
    return render(request,'index.html',context)
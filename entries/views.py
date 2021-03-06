from django.shortcuts import render, redirect
from .models import Entry
from entries.forms import EntryForm

def index(request):
    entries = Entry.objects.order_by('-date_posted')
    print('***')
    context = {
        'entries' : entries
    }
   
    return render(request, 'index.html', context)

def add(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EntryForm()

    context = {'form' : form}

    return render(request, 'entries/add.html', context)
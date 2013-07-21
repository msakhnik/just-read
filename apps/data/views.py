from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from apps.data.models import Entry
from apps.data.forms import DataForm
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseNotFound

@login_required
def add(request):
    form = None
    if request.method == 'POST':
        form = AddBookForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.title = request.title
            instance.text = request.text
            instance.save()
    else:
        form = AddBookForm()

    ctx = {
        'form': form
    }
    return render_to_response('data/create.html', ctx, context_instance=RequestContext(request))

@login_required
def entry(request, id):
#    try:
    entrie = Entry.objects.get(id=id)
    ctx = {'entrie': entrie}
    return render_to_response('data/entry.html', ctx, context_instance=RequestContext(request))
#    except:
#        return HttpResponse('<h1>Page was found</h1>')

@login_required
def create(request):
    a = Entry()

    form = DataForm(request.POST or None)
    if form.is_valid():
        form.save()


    ctx = {
        'form': form
    }
    return render_to_response('data/create.html', ctx, context_instance=RequestContext(request))
# Create your views here.

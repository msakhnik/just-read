from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from apps.data.models import Entry
from apps.data.forms import DataForm
from django.conf import settings
from django.core.urlresolvers import reverse

@login_required
def create(request):
    a = Entry()
    form = DataForm(request.POST or None)
    print "Some form"
    print form

    if form.is_valid():
        print form
        return redirect(reverse('accounts_profile'))

    ctx = {
        'form': form
    }
    return render_to_response('data/create.html', ctx, context_instance=RequestContext(request))
# Create your views here.

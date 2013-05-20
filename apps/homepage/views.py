from django.shortcuts import render_to_response
from apps.data.models import Entry
from django.template import RequestContext
from apps.homepage.forms import ContactForm

import smtplib

from django.views.decorators.csrf import csrf_exempt

def index(request):
    entries = Entry.objects.published_entries().order_by('-id')
    ctx = {'entries': entries}
    return render_to_response('homepage/index.html', ctx, context_instance=RequestContext(request))

def about(request):
    return render_to_response('homepage/about.html', context_instance=RequestContext(request))

@csrf_exempt
def contact(request):

    success = False
    email = ""
    title = ""
    text = ""
    contact_sent =  request.session.get('contact_sent')
    if request.method == "POST":
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            success = True
            email = contact_form.cleaned_data['email']
            title = contact_form.cleaned_data['title']
            text = contact_form.cleaned_data['text']
            request.session['contact_sent'] = True
# FIXME: email notification
#            to = 'kskster@gmail.com'
#            user = 'misha-tester@yandex.ru'
#            pwd = '*******'
#            smtpserver = smtplib.SMTP("213.180.204.38", 25)
#            smtpserver.ehlo()
#            smtpserver.starttls()
#            smtpserver.ehlo
#            smtpserver.login(user, pwd)
#            header = 'To:' + to + '\n' + 'From: ' + user + '\n' + 'Subject:testing \n'
#            print header
#            msg = header + '\n  \n\n'
#            msg += 'Email:' + email + '\nTitle: ' + title + '\nText: ' + text
#            smtpserver.sendmail(user, to, msg)
            print 'done!'
#            smtpserver.close()
    else:
        contact_form = ContactForm()

    ctx = {'contact_form': contact_form, 'contact_sent': contact_sent, 'email' : email, 'title': title, 'text': text, 'success': success}

    return render_to_response('homepage/contact.html', ctx, context_instance=RequestContext(request))

def archive(request):
    return render_to_response('homepage/archive.html', context_instance=RequestContext(request))
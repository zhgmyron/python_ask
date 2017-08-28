# -*- coding: UTF-8 -*-

from django.http import HttpResponse,Http404
from django.shortcuts import render
import datetime

def hello(request):
    return HttpResponse("Hello world")


def current_datetime(request):
    dt= datetime.datetime.now()
    return render(request, 'exercise/current_datetime.html',{'current_date':dt})
def hours_ahead(request,offset):
    try:
        offset= int(offset)
    except ValueError:
        raise Http404
    dt= datetime.datetime.now() + datetime.timedelta(hours=offset)

    return render(request, 'exercise/hours_ahead.html',{'hour_offset':offset,'next_time':dt})
def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form':
form})
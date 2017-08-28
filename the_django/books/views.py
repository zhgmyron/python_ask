# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django import forms
from django.core.mail import send_mail
from django.http import HttpResponse,HttpResponseRedirect
from books.models import Book

def current_url_view_good(request):
    values = request.META.items()

    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def search_form(request):
    return render(request, 'books/search_form.html')

def search(request):
    errors = []
    if 'q' in request.GET:
        q= request.GET['q']
        if not q:
            errors.append('enter search term.')
        elif len(q) >15:
            errors.append('please enter at most 15 character.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request,'books/search_results.html',
                          {'books':books,'query':q})

    return render(request,'books/search_form.html',{'errors':errors})

class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField(required=False)
    message = forms.CharField()
# def contact(request):
#     errors =[]
#     if request.method == 'POST':
#         if not request.POST.get('subject',''):
#             errors.append('Enter a subject.')
#         if not request.POST.get('message', ''):
#             errors.append('Enter a message.')
#         if request.POST.get('email') and '@' not in request.POST['email']:
#             errors.append('Enter a valid email address.')
#         if not errors:
#             send_mail(
#                 request.POST['subject'],
#                 request.POST['message'],
#                 request.POST.get('email', 'noreply@example.com'),
#                 ['siteowner@example.com'],
#             )
#             return HttpResponseRedirect('/contact/thanks/')
#     return render(request,'books/contact_form.html',
#                   {'errors': errors,
#                    'subject':request.POST.get('subject',''),
#                    'message':request.POST.get('message',''),
#                    'email':request.POST.get('email','')
#                    })

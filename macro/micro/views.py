from django.shortcuts import render
from django.http import HttpResponse
from .email_utils import emails
from .models import Contact

# Create your views here.

def index(request):
    return render(request,'index.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('text', '')  # Ensure this matches your form's input name attribute
        message = request.POST.get('message', '')
        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()
        return HttpResponse("<h1>Thanks for contacting us!</h1>")
    return render(request, 'contact.html')

def products(request):
    return render(request, 'products.html')

def about(request):
    return render(request, 'about.html')

def emails(request):
    
    subject = 'Premium Notifications'
    recipient_list = ['francisnjaramba2@gmail.com']
    template_name = 'email.html'
    context = {'username': 'Team member', 'verification_link': 'http://example.com/verify/123/'}

    emails(subject, recipient_list, template_name, context)
    return HttpResponse("Email with Template Sent Successfully!")
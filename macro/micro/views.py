from django.shortcuts import render, redirect
from django.http import HttpResponse
from .email_utils import emails
from .models import Contact, Products, Customer
from django.contrib import messages
from django.template.loader import render_to_string


def index(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')  # Ensure this matches your form's input name attribute
        message = request.POST.get('message', '')
        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()
        return HttpResponse("<h1>Thanks for contacting us!</h1>")
    return render(request, 'contact.html')


def products(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            try:
                Customer.objects.create(email=email)
                # return HttpResponse("<h1>Thanks for contacting us!</h1>")
                html_content = render_to_string('thankyou.html', {'request': request})
                return HttpResponse(html_content)
                # messages.success(request, 'Thank you! We will follow up with you.')
                # return redirect('buy_now')  # Redirect to the same page after submission
            except Exception as e:
                messages.error(request, f'Error saving email: {e}')
        else:
            messages.error(request, 'Email address is required.')
    # Example commented-out code for creating Products instances
    # products1 = Products()
    # products1.desc = 'Feel the flavour'
    # products1.price = 1200
    # products1.images = '/cup3.jpg'
    # products2 = Products()
    # products2.desc = 'Feel the flavour'
    # products2.price = 1200
    # products2.images = '/cup4.jpeg'
    # products3 = Products()
    # products3.desc = 'Feel the flavour'
    # products3.price = 1200
    # products3.images = '/mindful.jpg'
    # products = [products1, products2, products3]

    products = Products.objects.all()
    return render(request, 'products.html', {'products': products})


def about(request):
    return render(request, 'about.html')


def emails(request):
    subject = 'Premium Notifications'
    recipient_list = ['francisnjaramba2@gmail.com']
    template_name = 'email.html'
    context = {'username': 'Team member', 'verification_link': 'http://example.com/verify/123/'}

    emails(subject, recipient_list, template_name, context)
    return HttpResponse("Email with Template Sent Successfully!")


# def buy_now(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         if email:
#             try:
#                 Customer.objects.create(email=email)
#                 messages.success(request, 'Thank you! We will follow up with you.')
#                 return redirect('buy_now')  # Redirect to the same page after submission
#             except Exception as e:
#                 messages.error(request, f'Error saving email: {e}')
#         else:
#             messages.error(request, 'Email address is required.')
#     return render(request, 'order.html')




def contact_success(request):
    html_content = render_to_string('thank_you.html', {'request': request})
    return HttpResponse(html_content)


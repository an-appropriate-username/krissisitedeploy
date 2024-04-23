from django.shortcuts import redirect, render
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            details = f'Enquiry from: {form.cleaned_data["name"]}'
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            message = form.cleaned_data["message"]
            photo = form.cleaned_data["photo"]
            availability = form.cleaned_data["availability"]
            web_link = "https://krissisitedeploy.onrender.com/admin/login/"

            send_mail(details, #subject
                        f"NAME:\n {form.cleaned_data['name']}\n\n PHONE:\n {phone}\n\n EMAIL:\n {email}\n\n MESSAGE:\n {message}\n\n PHOTO:\n {photo.url}\n\n AVAILABILITY:\n {availability}\n\n VIEW FULL ENQUIRY:\n{web_link}",  #message
                        None, # from
                        settings.ADMIN_EMAILS) #to
            return redirect ('success')

    form = ContactForm()
    context = {'form': form}
    return render(request, "kuw/home.html", context)

def faq(request):
    return render(request, "kuw/faq.html")

def success(request):
    return render(request, "kuw/success.html")

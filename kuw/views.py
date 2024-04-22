from django.shortcuts import render
from .forms import ContactForm

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

    form = ContactForm()
    context = {'form': form}

    return render(request, "kuw/home.html", context)

def faq(request):
    return render(request, "kuw/faq.html")
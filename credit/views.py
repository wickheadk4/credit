from django.shortcuts import render, redirect
from django.core.mail import send_mail
# from django.conf import settings

# Create your views here.
receiver = "hypercreditfix@gmail.com"
def index(request):

    return render(request, "credit/index.html")


def about(request):

    return render(request, "credit/about.html")


def contact(request):

    return render(request, "credit/contact.html")


def services(request):

    return render(request, "credit/services.html")

def mess(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        subject = request.POST.get("subject")
        final = f"{name}, \n\n{message}"
        # email_from = settings.EMAIL_HOST_USER
        recipient_list = [receiver, ]
        send_mail(subject, final, email, recipient_list)

        return redirect("/")
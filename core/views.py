from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact_us(request):
    if request.method == 'POST':
        # handle form submission
        pass
    return render(request, 'contact.html')

def security_services(request):
    return render(request, 'security_services.html')

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

def night_patrolling(request):
    return render(request, 'night_patrolling.html')

def facility_management(request):
    return render(request, 'facility_management.html')

def training(request):
    return render(request, 'training.html')

def deployment(request):
    return render(request, 'deployment.html')

def supervision(request):
    return render(request, 'supervision.html')

def recruitment(request):
    return render(request, 'recruitment.html')

def camera_monitoring(request):
    return render(request, 'camera_monitoring.html')


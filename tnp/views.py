from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Studentdetails, Placements
# Create your views here.
def index(request):
    stu_details = Studentdetails.objects.all()
    return render(request, 'index.html', {'stu_details': stu_details})

def about(request):
    return render(request, 'about.html')

def training(request):
    return render(request, 'training.html')

def placements(request):
    place_det = Placements.objects.all()
    if request.method == 'POST':
        comp=request.POST.get('comp')
        stu_details = Studentdetails.objects.all()
        return render(request, 'placements.html', {'place_det': place_det,'stu_details':stu_details,'comp':comp})
    return render(request, 'placements.html',{'place_det': place_det})
    
def contact(request):
    return render(request, 'contact.html')

def register(request):
    if request.method == 'POST':
        roll_number = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email exists')
                return redirect('register')
            elif Studentdetails.objects.filter(roll_number=roll_number).exists() == False:
                messages.info(request, 'Your details are not found')
                return redirect('register')
            else:
                user = User.objects.create_user(username=roll_number, email=email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'Passwords not same')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        roll_number = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(password=password,username=roll_number)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Info Invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

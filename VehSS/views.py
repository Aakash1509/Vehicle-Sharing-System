import queue
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.core.mail.message import EmailMessage
from django.conf import settings
from django.core import mail
from django.contrib import messages
# from .models import VehSS
from .forms import OwnerForm
# from .forms import TravellerForm
from VehSS.models import Owner
from VehSS.models import Summary
from django.db.models import Q
from django.http import JsonResponse

# from VehSS.models import Manager


# def manager(request):
#     # submitted=False
#     if request.method=="POST":
#         name = request.POST.get('name')
#         email_address = request.POST.get('email_address')
#         location = request.POST.get('location')
#         carname = request.POST.get('carname')
#         seats = request.POST.get('seats')
#         phone = request.POST.get('phone')
#         date_time = request.POST.get('date_time')
#         image = request.POST.get('image')
#         en=Owner(name=name,email_address=email_address,location=location,carname=carname,seats=seats,phone=phone,date_time=date_time,image=image)
#         en.save()
#     return render(request,'owner.html')

# def send_email():
#     # submitted=False
#     from django.core.mail import send_mail

#     send_mail(
#     'Subject here',
#     'Here is the message.',
#     'from@example.com',
#     ['x'],
#     fail_silently=False,
# )


def owner(request):
    # submitted=False
    # from django.core.mail import send_mail

    # send_mail(
    # 'Testing mail',
    # 'Here is the message.',
    # 'info.vss163@gmail.com',
    # ['21cs053@charusat.edu.in'],
    # fail_silently=False,
    # )
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        # email_address = request.POST.get('email_address')
        location = request.POST.get('location')
        carname = request.POST.get('carname')
        seats = request.POST.get('seats')
        phone = request.POST.get('phone')
        date_time = request.POST.get('date_time')
        image = request.FILES['image']
        en=Owner(name=name,email=email,location=location,carname=carname,seats=seats,phone=phone,date_time=date_time,image=image)
        en.save()
         
        # messages.success(request,"Owner registered succesfully")
    return render(request,'owner.html')
    # else:
    #     form=OwnerForm
    #     if 'submitted' in request.GET:
    #         submitted=True
    

def traveller_v(request):
    # submitted=False
    # if request.method=="POST":
    #     form = TravellerForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect('/traveller?submitted=True')
    # else:
    #     form=OwnerForm
    #     if 'submitted' in request.GET:
    #         submitted=True
    ownerData=Owner.objects.all()
    data={
        'ownerData' : ownerData
    }

    # emails sending starts from here
    # from_email=settings.EMAIL_HOST_USER
    # connection=mail.get_connection()
    # connection.open()
    # email_message=mail.EmailMessage(f'Email from {request.user} ', f'The traveller will join you from {n.location} at {n.date_time}',from_email,[{n.email}],connection=connection)
    # connection.send_messages([email_message])
    # connection.close()
    

    # send_email()
    return render(request,'traveller_v.html',data)


def traveller_a(request):
    ownerData=Owner.objects.all()
    data={
        'ownerData' : ownerData
    }
    
    return render(request,'traveller_a.html',data)

def traveller_n(request):
    ownerData=Owner.objects.all()
    data={
        'ownerData' : ownerData
    }
    
    return render(request,'traveller_n.html',data)

# Create your views here.
# from .forms import OrderForm,CreateUserForm

def registerPage(request):
    form=UserCreationForm()

    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # message.success("You have registered succesfully")
            return redirect("/login")
    context={'form':form}
    
    # return HttpResponse("You have registered successfully !!!")
    
    return render(request,'register.html',context)


def index1(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index1.html')


def traveller(request):
    return render(request, 'traveller.html')

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def formu(request):
    return render(request, 'form.html')


def services(request):
    return render(request, 'services.html')

def userview(request):
    ownerData=Owner.objects.all()
    data={
        'ownerData' : ownerData
    }
    return render(request, 'userview.html',data)


def contact(request):
    return render(request, 'contact.html')


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
          # A backend authenticated the credentials
          login(request,user)
          return redirect("/")
        else:
          # No backend authenticated the credentials
          return redirect(request, 'login.html')
    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect("/login")

def add_vehicle(request):
    # t_name = request.user
    # o_name=request.GET.get('owner_name')
    # emaill=Owner.objects.get(id=o_name)
    # loc=Owner.objects.get(id=o_name)
    # phone=Owner.objects.get(id=o_name)
    # date_time=Owner.objects.get(id=o_name)
    # Summary(traveller_name=t_name,owner_name=o_name,email=emaill,location=loc,phone=phone,date_time=date_time).save()
    t_name = request.GET.get('traveller_name')
    o_name = request.GET.get('owner_name')
    email = request.GET.get('email')
    # email_address = request.POST.get('email_address')
    location = request.GET.get('location')
    phone = request.GET.get('phone')
    date_time = request.GET.get('date_time')
    image = request.GET.get('image')
    en=Summary(traveller_name=t_name,owner_name=o_name,email=email,location=location,phone=phone,date_time=date_time,image=image)
    en.save()
    # send_email(email)
    from_email=settings.EMAIL_HOST_USER
    connection=mail.get_connection()
    connection.open()
    email_message=mail.EmailMessage(f'Email from {t_name}',f'{t_name} wants to travel with you from {location} on {date_time}',from_email,[email],connection=connection)
    connection.send_messages([email_message])
    connection.close()
    return redirect('/summary')

def summary(request):
    if request.user.is_authenticated:
        user=request.user
        vehicle=Summary.objects.filter(traveller_name=user)
        return render(request,'summary.html',{'data':vehicle})


def minusvehicle(request):
    if request.method=='GET':
        seats = request.GET['seats']
        c=Owner.objects.get(Q(seats=seats))
        c.seats-=1
        c.save()
    data={
        'seats':c.seats
    }
    return JsonResponse(data)

def gotit(request):
    return render(request, 'gotit.html')
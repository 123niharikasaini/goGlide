from django.shortcuts import render,HttpResponse,redirect
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from core.models import Customer,Driver,Booking,Rent_info
# Create your views here.

@login_required(login_url="signin")
def index(request):
    return render(request,"index.html")

def signin(request):
    # signin the user
    if request.method=="POST":
        username=request.POST['uname']
        password=request.POST['pass']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Credentials invalid')
            return redirect("signin")

    else:
        return render(request,'login.html')
    

def mid(request):
    return render(request,"midConfirm.html")
    
def signup(request):
    if request.method=="POST":
        username=request.POST['uname']
        fname=request.POST['f_name']
        lname=request.POST['l_name']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        contact=request.POST['contact']
        gender=request.POST['gender']


        if pass1==pass2:
            # check all objects in User table and then filter on the basis of the email
            if User.objects.filter(email=email).exists():
                # if already exists
                messages.info(request,'Email taken')
                return redirect("signup")
            elif User.objects.filter(username=username).exists():
                messages.info(request,"Username taken")
                return redirect("signup")
            else:
                # creating the user
                user=User.objects.create_user(username=username,first_name=fname,last_name=lname,email=email)
                user.save()
                # log user in and redirect to settings page
                # user_login=auth.authenticate(username=username,password=pass1)
                auth.login(request,user)

                # create a profile object for new user
                user_model=User.objects.get(username=username)
                new_profile=Customer.objects.create(user=user_model,name=user_model.first_name+user_model.last_name,email_id=user_model.email,contact_no=contact,gender=gender)
                new_profile.save()
                return redirect("/")
        else:
            messages.info(request,"Password not matching")
            return redirect('signup')
        # print(username)
    else:
        return render(request,'signup.html')
    
def driverdetails(request):
    if request.method=="POST":
        username=request.POST['uname']
        fname=request.POST['f_name']
        lname=request.POST['l_name']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        contact=request.POST['contact']
        gender=request.POST['gender']
        dob=request.POST['dob']
        add=request.POST['address']
        licenceNo=request.POST['licenceNo']
        vehicleNo=request.POST['vehicleNo']
        vehicleType=request.POST['vehicleType']

        if pass1==pass2:
            # check all objects in User table and then filter on the basis of the email
            if User.objects.filter(email=email).exists():
                # if already exists
                messages.info(request,'Email taken')
                return redirect("driverdetails")
            elif User.objects.filter(username=username).exists():
                messages.info(request,"Username taken")
                return redirect("driverdetails")
            else:
                # creating the user
                user=User.objects.create_user(username=username,first_name=fname,last_name=lname,email=email)
                user.save()
                # log user in and redirect to settings page
                # user_login=auth.authenticate(username=username,password=pass1)
                auth.login(request,user)

                # create a profile object for new user
                user_model=User.objects.get(username=username)
                new_profile=Driver.objects.create(user=user_model,name=user_model.first_name+" "+user_model.last_name,contact_no=contact,gender=gender,email_id=user_model.email,address=add,licence_no=licenceNo,vehicle_no=vehicleNo,vehicle_type=vehicleType,D_O_B=dob)
                new_profile.save()
                return redirect("driverLogin")
        else:
            messages.info(request,"Password not matching")
            return redirect('driverdetails')
        # print(username)
    else:
        return render(request,'driverdetails.html')


@login_required(login_url="signin")
def driverLogin(request):
    try:
        profile=Driver.objects.get(user=request.user)
        obj={'obj':profile}
        return render(request,'driverLogin.html',obj)
    except Driver.DoesNotExist:
        # if not exit, throw an error
        return render(request,'index.html')

    

def book(request):
    if request.method=="POST":
        msg=""
        name=request.POST["name"]
        phone=request.POST["phone"]
        pin=request.POST["pin"]
        location=request.POST["location"]

        user=request.user #currnetly logged is user
        # user_model=User.objects.get(username=username)
        book_model=Booking.objects.create(user=request.user,name=name,number=phone,pin=pin,location=location)
        book_model.save()
        return render(request,"submit.html",{msg:"Data Successfully saved"})
    else:
        return HttpResponse("Not working")

def rent(request):
    if request.method=="POST":
        msg=""
        name=request.POST["name"]
        phone=request.POST["phone"]
        pin=request.POST["pin"]
        location=request.POST["location"]
        date=request.POST["date"]
        timeDuration=request.POST["timeDuration"]
        time=request.POST["start_time"]

        user=request.user #currnetly logged is user
        # user_model=User.objects.get(username=username)
        rent_model=Rent_info.objects.create(user=request.user,name=name,number=phone,pin=pin,location=location,dateBooked=date,timeDuration=timeDuration,startTime=time)
        rent_model.save()
        return render(request,"submit.html",{msg:"Data Successfully saved"})
    else:
        return HttpResponse("Not working")

@login_required(login_url="signin")
def submit(request):
    return render(request,"submit.html")

@login_required(login_url="signin")
def signOut(request):
    auth.logout(request)
    return redirect("signin")


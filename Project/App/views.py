from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import *
from django.db.models import Q



def home(request):
    videos = Video.objects.all()
    # visitor = Visitor.objects.filter(id=1).first()
    # visitor.visit = visitor.visit + 1
    # visitor.save()
    # userinfo=Userinfo.objects.all()

    def get_ip(request):
        address = request.META.get('HTTP_X_FORWARDED_FOR')
        if address:
            ip=address.split(',')[-1].strip()
        else:
            ip=request.META.get('REMOTE_ADDR')
        return ip

    ip=get_ip(request)
    u=Visitor(visit=ip)
    print(ip)
    result=Visitor.objects.filter(Q(visit__icontains=ip))
    if len(result)==1:
        print("user exist")
    elif len(result)>1:
        print("user exist more...")
    else:
        u.save()
        print("user is unique")

    count=Visitor.objects.all().count()

    return render(request,'app/home.html', {'videos':videos,'count':count})



######LOGIN & REGISTER#######


def loginuser(request):
    if request.method=='GET':
        return render(request,'app/loginuser.html', {'form':AuthenticationForm(),'form2':CreateUserForm()})
    else:
        user= authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'app/loginuser.html', {'form':AuthenticationForm(),'error':'Enter Correct Info','form2':CreateUserForm()})
        else:
            login(request,user)
            return redirect('home')


@login_required
def logoutuser(request):
    if request.method=='POST':
        logout(request)
        return redirect('home')


def signupuser(request):

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
            
			admin = form.save()
			username = form.cleaned_data.get('username')

			Userinfo.objects.create(
				admin=admin,
				name=request.POST.get('name'),
                email=admin.email,
                contact_no=request.POST.get('contact_no'),
				)
			admin.save()
			login(request,admin)
			return redirect('home')			
	return redirect('loginuser')


def index(request):
    userinfo=Userinfo.objects.all()

    def get_ip(request):
        address = request.META.get('HTTP_X_FORWARDED_FOR')
        if address:
            ip=address.split(',')[-1].strip()
        else:
            ip=request.META.get('REMOTE_ADDR')
        return ip

    return render(request,'app/')

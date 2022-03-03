from email import message
from plistlib import UID
from django.shortcuts import render,redirect
from onlineshopapp.models import register
from django.contrib import messages
# Create your views here.
def registeraction(request):
    if 'uid' in request.session:
        return redirect('home')
    message={}
    
    if request.method=="POST":
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        email=request.POST['email']
        email=request.POST['email']
        adr=request.POST['adress']
        pwd=request.POST['password']
        cpwd=request.POST['cpassword']
        gen=request.POST['gender']
        country=request.POST['country']
        image=request.FILES.get('image')
        # try:
        #     image=request.FILES['image']    
        # except:
        #     if gen=="Male":
        #         image='static/images/default male prof.jpg'
        #     else:
        #         image='static/images/default female prof.jpg'#
        if pwd==cpwd:
            if register.objects.filter(email=email).exists():
                messages.info(request,'The user is already exists')
            else:
                re=register(firstname=fname,lastname=lname,email=email,adress=adr,password=pwd,gender=gen,countrty=country,profile_image=image)
                re.save()
                return redirect('login')
        else:
            messages.info(request,'username or Password incorrects')       
    return render(request,'registeraction.html',message,)


def login(request):
    message={}
    if 'uid' in request.session:
        return redirect('home')
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        if register.objects.filter(email=email,password=password).exists():
            regi=register.objects.get(email=email)
            print("The user id number is",regi)
            request.session['uid']=regi.id
            
            return redirect('home')
        else:
            messages.info(request,  'Incorect username or password')
            return redirect('login')
    return render(request,'login.html',message)

def home(request):
    if 'uid' in request.session:
        user=register.objects.get(id=request.session['uid'])
        return render(request,'home.html',{'user':user})
    else:
        return redirect('login')

def logout(request):
    del request.session['uid']
    request.session.flush()
    return redirect('login')
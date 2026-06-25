from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import*
from datetime import datetime
# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def gallery(request):
    return render(request,"gallery.html")

def contact(request):
    return render(request,"contact.html")

def team(request):
    return render(request,"team.html")
def category(request):
    return render(request,"category.html")

def services(request):
    return render(request,"services.html")

def login(request):
    if request.method=="POST":
        email=request.POST.get("email")#abc@gmail.com
        password=request.POST.get("passwd")#1
        x=tblregister.objects.all().filter(email=email,password=password)
        if x.count()==1:
            request.session["name"]=str(x[0].name)
            request.session["userpic"]=str(x[0].picture)
            b=x[0].batch
            if b:
                request.session["batch"]=str(x[0].batch.id)
            request.session["email"]=email
            
            return HttpResponse("<script>alert('you are login successfully..');location.href='/student/dashboard/'</script>")
        else:
            return HttpResponse("<script>alert('your Email Id or Password is Incorrect.');location.href='/login/'</script>")
        
    return render(request,"login.html")

def register(request):
    if request.method=="POST":
        Name=request.POST.get("name")
        Email=request.POST.get("email")
        Mobile=request.POST.get("mob")
        Password=request.POST.get("passwd")
        
        Address=request.POST.get("address")
        Picture=request.FILES["fu"]
        tblregister(name=Name,email=Email,mobile=Mobile,password=Password,address=Address,picture=Picture,regdate=datetime.now().date()).save()
        return HttpResponse("<script>alert('You are Registered Successfully');location.href='/register'</script>")
    return render(request,"register.html")


def logout(request):
    user=request.session.get("email")
    if user:
        del request.session["email"]
        return redirect("/login/")
    
    return render(request,"logout.html")

    


def lectures(request):
    return render(request,"lectures.html")

def lecturecat(request):
    return render(request,"lecturecat.html")

def enotes(request):
    return render(request,"enotes.html")

def dashboard(request):
    return render(request,"dashboard.html")

def profile(request):
    return render(request,"profile.html")

def softwarekit(request):
    return render(request,"softwarekit.html")

def Category(request):
    return render(request,"category.html")






















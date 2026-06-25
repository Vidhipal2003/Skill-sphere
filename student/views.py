from django.shortcuts import render,redirect
from user.models import *
from django.http import HttpResponse

# Create your views here.
def dashboard(request):
    return render(request,"student/dashboard.html")

def mycategory(request):
    return render(request,"student/category.html")


def lectures(request):
    data=mylecture.objects.all()
    d={"vdo":data}
    return render(request,"student/lectures.html",d)

def lecturecat(request):
    bid=request.session.get("batch")
    cat=Category.objects.all().filter(batch_name=bid)
    d={"categories":cat}
    return render(request,"student/lecturecat.html")


def enotes(request):
    bid=request.session.get("batch")
    data=notes.objects.all().filter(batch=bid)
    d={"notes":data}

    return render(request,"student/enotes.html",d)



def profile(request):
    user=request.session.get("email")#xyz@gmail.com
    data=tblregister.objects.all().filter(email=user)
    d={"userinfo":data}
    return render(request,"student/profile.html",d)
    


def signout(request):
    return render(request,"student/signout.html")
 


def softwarekit(request):
    data=softwarekit.objects.all()
    d={"sdata":data}

    return render(request,"student/softwarekit.html",d)

def task(request):
    bid=request.session.get("batch")
    data=mytask.objects.all().filter(batch=bid)
    d={"data":data}
    return render(request,'student/task.html',d)

def tsubmitted(request):
    userid=request.session.get("email")
    if request.method=="POST":
        title=request.POST.get("title")
        tid=request.POST.get("tid")
        taskfile=request.FILES["fu"]
        x=submittedtask.objects.all().filter(userid=userid,tid=tid).count()
        if x==1:
            return HttpResponse("<sript>alert('your task is already submitted..');location.href='student/task/</script>")
        else:
             submittedtask(title=title,tid=tid,upload_task=taskfile,userid=userid).save()
             return HttpResponse("<sript>alert('your task is submitted ssuccessfully..');location.href='student/task/'</script>")

    return render(request,"student/tsubmitted.html")




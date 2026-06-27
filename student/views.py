from django.shortcuts import render,redirect
from user.models import *
from django.http import HttpResponse

# Helper function to check login
def check_login(request):
    return request.session.get("email") is not None

# Create your views here.
def dashboard(request):
    if not check_login(request):
        return redirect("/login/")
    return render(request,"student/dashboard.html")

def mycategory(request):
    if not check_login(request):
        return redirect("/login/")
    return render(request,"student/category.html")


def lectures(request):
    if not check_login(request):
        return redirect("/login/")
    cat_id = request.GET.get('cat_id')
    bid = request.session.get("batch")
    if cat_id:
        data = mylecture.objects.all().filter(Category_id=cat_id, batch=bid)
    else:
        data = mylecture.objects.all().filter(batch=bid)
    d = {"vdo": data}
    return render(request,"student/lectures.html",d)

def lecturecat(request):
    if not check_login(request):
        return redirect("/login/")
    bid=request.session.get("batch")
    cat=Category.objects.all().filter(batch_name=bid)
    d={"categories":cat}
    return render(request,"student/lecturecat.html",d)


def enotes(request):
    if not check_login(request):
        return redirect("/login/")
    bid=request.session.get("batch")
    data=notes.objects.all().filter(batch=bid)
    d={"notes":data}
    return render(request,"student/enotes.html",d)


def profile(request):
    if not check_login(request):
        return redirect("/login/")
    user=request.session.get("email")#xyz@gmail.com
    data=tblregister.objects.all().filter(email=user)
    d={"userinfo":data}
    return render(request,"student/profile.html",d)
    

def signout(request):
    if request.session.get("email"):
        request.session.flush()
    return redirect("/logout/")
 


def softwarekit(request):
    if not check_login(request):
        return redirect("/login/")
    data=softwareKit.objects.all()
    d={"sdata":data}
    return render(request,"student/softwarekit.html",d)

def task(request):
    if not check_login(request):
        return redirect("/login/")
    bid=request.session.get("batch")
    userid=request.session.get("email")
    tasks=mytask.objects.all().filter(batch=bid)
    submitted_ids = list(submittedtask.objects.all().filter(userid=userid).values_list('tid', flat=True))
    for t in tasks:
        t.is_submitted = t.id in submitted_ids
        sub = submittedtask.objects.all().filter(userid=userid, tid=t.id).first()
        t.marks = sub.marks if sub else None
    d={"data":tasks}
    return render(request,'student/task.html',d)

def tsubmitted(request):
    if not check_login(request):
        return redirect("/login/")
    userid=request.session.get("email")
    if request.method=="POST":
        title=request.POST.get("title")
        tid=request.POST.get("tid")
        taskfile=request.FILES["fu"]
        x=submittedtask.objects.all().filter(userid=userid,tid=tid).count()
        if x==1:
            return HttpResponse("<script>alert('your task is already submitted..');location.href='/student/task/'</script>")
        else:
             submittedtask(title=title,tid=tid,upload_task=taskfile,userid=userid).save()
             return HttpResponse("<script>alert('your task is submitted successfully..');location.href='/student/task/'</script>")

    return render(request,"student/tsubmitted.html")




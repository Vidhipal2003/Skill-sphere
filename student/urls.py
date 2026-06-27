from django.urls import path 
from.import views

urlpatterns = [
path("category/",views.mycategory),
path("lectures/",views.lectures),
path("lecturecat/",views.lecturecat),
path("enotes/",views.enotes),
path("dashboard/",views.dashboard),
path("profile/",views.profile),
path("softwarekit/",views.softwarekit),
path("signout/",views.signout),
path("task/",views.task),
path("tsubmitted/",views.tsubmitted),
]
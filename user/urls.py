from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),
    path("index/",views.index),
    path("about/",views.about),
    path("gallery/",views.gallery),
    path("category/",views.Category),
    path("contact/",views.contact),
    path("team/",views.team),
    path("services/",views.services),
    path("login/",views.login),
    path("register/",views.register),
    path("lecturecat/",views.lecturecat),
    path("profile/",views.profile),
    path("softwarekit/",views.softwarekit),
    path("logout/",views.logout),
    
]


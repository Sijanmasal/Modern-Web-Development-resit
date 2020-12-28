from django.urls import path
from home import views
urlpatterns = [
    path('',views.index),
    path('register',views.register),
    path('login',views.login),
    path('logout',views.logout),
    path('about',views.about),
    path('accomodation',views.accomodation),
    path('blog',views.blog),
    path('blog-single',views.blog_single),
    path('contact',views.contact),
    path('elements',views.elements),
    path('gallery',views.gallery),
]
from django.urls import path
from . import views
urlpatterns = [

    path('home/', views.home, name='dani'),
    path("", views.homepage, name="homepage"),
    # path('ali/', views.ali, name='ali'),
    path('about/',views.about,name='about'),
    path('blog/',views.blog,name='blog'),
    path('contact/',views.contact,name='contact'),
    path('ali/<slug:code>/', views.alidetails, name='alidetails'),

    
]
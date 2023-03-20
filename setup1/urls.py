
from django.urls import path,include
from . import views
urlpatterns = [
    #path('', views.index, name = 'index'),
    path('',views.home,name = 'home'),
    path('^transfer/$',views.transfer,name='transfer'),
    path('^customer$',views.customer,name='customer'),
    
]
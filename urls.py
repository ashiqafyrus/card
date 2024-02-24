from django.urls import path,include
from .import views
urlpatterns = [
   path('',views.home,name='home'),
   path('about',views.about,name='about'),
   path('services',views.services,name='services'),
    path('login',views.login,name='login'),
    path('crmpage',views.crmpage,name='crmpage'),
    path('crmcontent',views.crmcontent,name='crmcontent'),
    path('drag',views.drag,name='drag')]
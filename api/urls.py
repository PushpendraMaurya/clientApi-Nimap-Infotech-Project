from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework import routers


router= routers.DefaultRouter()
router.register(r'clients', views.ClientViewSet)
router.register(r'project', views.ProjectViewSet)

urlpatterns = [    
    path('',include(router.urls))
      
]


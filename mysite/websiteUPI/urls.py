from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about', views.about, name = 'about'),
    path('upi', views.upi, name = 'upi'),
    # path('getFile', views.getFile, name = 'getFile'),
]

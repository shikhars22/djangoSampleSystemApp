from tkinter import LAST
from django.shortcuts import render
from django.http import HttpResponse  
from websiteUPI.functions import handle_uploaded_file
from .models import upiModel

# Create your views here.
def index(request):
    return render(request, 'index.html' , {})

def about(request):
    return render(request, 'about.html' , {})

def upi(request):
    if request.method == 'POST':
        uploadedFile = request.FILES['document']
        print(uploadedFile.name)
        print(uploadedFile.size)
        fileCreateVar=upiModel.objects.create(file=uploadedFile, description="Test SKG")
        fileCreateVar.save()
    return render(request, 'upi.html' , {})

# def getFile(request):
#     getAllObjects = upiModel.objects.all()
#     getLatestObject = upiModel.objects.filter(id = 3)
#     print(dir(getAllObjects))
#     print(getLatestObject.file)
#     return render(request, 'upi.html' , {})
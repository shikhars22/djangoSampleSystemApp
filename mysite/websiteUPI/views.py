import os
from _datetime import datetime, date
from email.message import EmailMessage
from smtplib import SMTPException
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

def getFile(request):
    getAllObjects = upiModel.objects.all()
    getLatestObject = upiModel.objects.latest('id')
    # print(dir(getAllObjects))
    print(getLatestObject.file)
    return render(request, 'upi.html' , {})

def sendOutput():
    try:    
        print("starting-----------------")
        super_dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        dir_path = os.path.dirname(os.path.realpath(__file__))
        print(dir_path)
        file_path = super_dir_path + '\\Input inputSuperBOMs in this excel.xlsm'
        print(file_path)
        path= r"C:\Users\guptash\OneDrive - Lam Research\Documents\bitbucket\djangoSampleApp\mysite\websiteUPI\businessLogic\Outputs\Unique Parts Output 2020-07-10 09.59 PM.xlsx"
        path=path.replace("\\","/")
        print(path)
        c=datetime.now()
        msg = EmailMessage('Testing-----------'+str(datetime.now()), 'Body of the email', 'shikhar.Gupta@lamresearch.com', ['shikhar.kumar@orbitsolutions.net'])
        msg.content_subtype = "html"
        file=open(path,'rb')
        msg.attach('test.xlsx',file.read(),'application/ms-excel')
        msg.send()
        print("mail sent------")
    except SMTPException as e:
        print("-------------0----------")
    return '-----Email Sent----'

sendOutput()
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

# def sendOutput():
#     try:    
#         print("starting-----------------")
#         super_dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
#         dir_path = os.path.dirname(os.path.realpath(__file__))
#         print(dir_path)
#         file_path = super_dir_path + '\\Input inputSuperBOMs in this excel.xlsm'
#         print(file_path)
#         path= r"C:\Users\guptash\OneDrive - Lam Research\Documents\bitbucket\djangoSampleApp\mysite\websiteUPI\businessLogic\Outputs\Unique Parts Output 2020-07-10 09.59 PM.xlsx"
#         path=path.replace("\\","/")
#         print(path)
#         c=datetime.now()
#         msg = EmailMessage('Testing-----------'+str(datetime.now()), 'Body of the email', 'shikhar.Gupta@lamresearch.com', ['shikhar.kumar@orbitsolutions.net'])
#         msg.content_subtype = "html"
#         file=open(path,'rb')
#         msg.attach('test.xlsx',file.read(),'application/ms-excel')
#         msg.send()
#         print("mail sent------")
#     except SMTPException as e:
#         print("-------------0----------")
#     return '-----Email Sent----'


def send_mail():
    path="D:\office\djangoSampleSystemApp\Forecast.csv"
    path=path.replace("\\","/")
    print("-------outlook -------")
    import win32com.client
    outlook = win32com.client.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = 'Sachit.Gupta@orbitsolutions.net'
    mail.Subject = 'Sample Email'
    mail.HTMLBody = '<h3>This is HTML Body</h3>'
    mail.Body = "This is the normal body"
    mail.Attachments.Add(path)
    # mail.CC = 'somebody@company.com'
    mail.Send()
    print("-----mail sent--------")

def email_send(path):
    try:
        print("-----------------")
        path="D:\office\djangoSampleSystemApp\Forecast.csv"
        path=path.replace("\\","/")
        c=datetime.now()
        msg = EmailMessage('Testing-----------'+str(datetime.now()), 'Body of the email', 'Sachit.Gupta@skylinesemi.com', ['Sachit.Gupta@orbitsolutions.net'])
        msg.content_subtype = "html"
        file=open(path,'rb')
        msg.attach('test.xlsx',file.read(),'application/ms-excel')
        msg.send()
        print("mail sent------")
        return '-----Email Sent----'
    except SMTPException as e:
        print("-------------0----------")
        return

def download_csv(request):    
    # file_path = os.path.join(settings.MEDIA_ROOT, 'example-input-file.txt')   
    file_path="D:\office\djangoSampleSystemApp\Forecast.csv" 
    if os.path.exists(file_path):    
        with open(file_path, 'rb') as fh:    
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")    
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)    
            return r
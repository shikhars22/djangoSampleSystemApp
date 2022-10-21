import os
from _datetime import datetime, date
# from email.message import EmailMessage
from django.core.mail import EmailMessage
from smtplib import SMTPException
from django.shortcuts import render
from django.http import HttpResponse  
from websiteUPI.functions import handle_uploaded_file
from .models import upiModel
import win32com.client
from django.core.mail import EmailMultiAlternatives


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



def send_mail(name=None):
    print(name,"--name----")
    super_dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)
    file_path = dir_path +r'\businessLogic\Outputs'+r'\Unique Parts Output 2020-07-10 09.59 PM.xlsx'
    print(file_path)
    path=file_path
    print("-------outlook -------")
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
# send_mail()
    

def email_send():
    try:
        # path="C:\\Users\jainkr\Videos\partdemand\PartHealth\Part Demand Output - 2022-05-04 05.51 PM - 1 parts analysis.xlsx"
       
        super_dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        dir_path = os.path.dirname(os.path.realpath(__file__))
        print(dir_path)
        file_path = dir_path +r'\businessLogic\Outputs'+r'\Unique Parts Output 2020-07-10 09.59 PM.xlsx'
        print(file_path)
        path=file_path
        c=datetime.now()
        msg = EmailMessage('Testing-----------'+str(datetime.now()), 'Body of the email', 'sachitgupta25@hotmail.com', ['Sachit.Gupta@orbitsolutions.net'])
        msg.content_subtype = "html"
        file=open(path,'rb')
        msg.attach('test.xlsx',file.read(),'application/ms-excel')
        msg.send()
        print("mail sent------")
        return '-----Email Sent----'
    except SMTPException as e:
        print("-------------0----------",e)
        return  
email_send()    
def download_csv(path):    
    # file_path = os.path.join(settings.MEDIA_ROOT, 'example-input-file.txt')   
    file_path=path
    if os.path.exists(file_path):    
        with open(file_path, 'rb') as fh:    
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")    
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)    
            return response
        
# send_mail()        

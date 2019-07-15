from django.http import HttpResponse
from django.shortcuts import render, redirect
import os,time,boto3
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.conf import settings
from .forms import CsvForm



def about(request):
    return render(request, 'fileconverter/about.html')


def csvtojson(request):
    if request.method == 'POST':
        form = CsvForm(request.POST, request.FILES)
        if form.is_valid():
           fileObject =  form.save()
           s3_client = boto3.client('s3', 
                      aws_access_key_id=settings.AWS_ACCESS_KEY_ID, 
                      aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY, 
                      region_name="eu-central-1"
                      )
           time.sleep(3)
           file_key = str(fileObject.id) + ".csv.json"
           bucket = "downloadjson"
           uri_duration = 90 #expiry duration in seconds. default 3600
           url = s3_client.generate_presigned_url('get_object', Params = 
           {'Bucket': bucket, 'Key': file_key}, ExpiresIn = uri_duration)
           
           
           return redirect(url)
    else:
        form = CsvForm()
    return render(request, 'fileconverter/csvtojson.html',{'form': form})



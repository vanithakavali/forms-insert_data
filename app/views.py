from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
def first(request):
    if request.method=='POST':
        USERNAME=request.POST['un']
        PASSWORD=request.POST['pw']
        print(USERNAME)
        print(PASSWORD)
        return HttpResponse('DATA IS SUBBMITTED')
    return render(request,'first.html')

def insert_topic(request):
    if request.method=="POST":
        tn=request.POST['topic']
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        return HttpResponse('insert_topic is done')
    return render(request,'insert_topic.html')
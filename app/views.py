from django.shortcuts import render
from app.models import *
# Create your views here.
def display_topics(request):
    QSTO=Topic.objects.all()
    d={'QSTO':QSTO}
    return render(request,'display_topics.html',d)

def display_web(request):
    QSWO=webpage.objects.all()

    QSWO=webpage.objects.all().filter(topic_name='cricket')
    QSWO=webpage.objects.all.filter(name__startswith='d')
    QSWO=webpage.objects.all.filter(url__edswith='com')
    QSWO=webpage.objects.all.filter(url__contains='www')
    QSWO=webpage.objects.all.filter(Q(name_contains='r')|Q(url__endswith('com')))
    d={'QSWO':QSWO}
    return render(request,'display_web.html',d)


def display_access(request):
    QSASO=access_records.objects.all()
    d={'QSASO':QSASO}
    return render(request,'display_access.html',d)






def insert_topic(request):
    tn=input('enter topic: ')
    To=Topic.objects.get_or_create(topic_name=tn)[0]
    To.save()

    QSTO=Topic.objects.all()
    d={'QSTO':QSTO}
    return render(request,'display_topics.html',d)


def insert_webpage(request):
    tn=input('enter topic: ')
    To=Topic.objects.filter(topic_name=tn)[0]
    To.save()
    n=input('enter name: ')
    u=input('enter url: ')
    Wo=webpage.objects.get_or_create(topic_name=To,name=n,url=u)[0]
    Wo.save()

    QSWO=webpage.objects.all()
    d={'QSWO':QSWO}
    return render(request,'display_web.html',d)




def insert_access(request):
    n=input('enter name: ')
    Wo=webpage.objects.filter(name=n)[0]
    Wo.save()

    d=input('enter date:')
    a=input('enter author: ')
    Ao=access_records.objects.get_or_create(name=Wo,date=d,author=a)[0]
    Ao.save()

    QSASO=access_records.objects.all()
    d={'QSASO':QSASO}
    return render(request,'display_access.html',d)







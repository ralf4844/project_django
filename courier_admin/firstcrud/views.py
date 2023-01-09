from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django. template import loader
from django.urls import reverse
from.models import addclients
from django.contrib import messages

# Create your views here.
def main(request):
    template=loader.get_template('main.html')
    return HttpResponse(template.render({},request))
    
def clients(request):
    myclients=addclients.objects.all().values()
    template=loader.get_template('clients.html')
    context={
        "myclients" : myclients,
    }
    return HttpResponse(template.render(context,request))

#def add(request):
 # template = loader.get_template('add.html')
  #return HttpResponse(template.render({}, request))
def add(request):

    a = request.POST['first']
    b = request.POST['last']
    c = request.POST['dni']
    d = request.POST['orig']
    e = request.POST['dest']
    f = request.POST['descrip']

    members=addclients(firstname=a,lastname=b, dni=c, origin=d, destiny=e, description=f)
    members.save()
        
    return HttpResponseRedirect(reverse('clients'))
   


def addrecord(request):
  if request.method == "POST":
    a = request.POST['first']
    b = request.POST['last']
    c = request.POST['dni']
    d = request.POST['orig']
    e = request.POST['dest']
    f = request.POST['descrip']

    members=addclients(firstname=a,lastname=b, dni=c, origin=d, destiny=e, description=f)
    members.save()
    
    return HttpResponseRedirect(reverse('clients'))

def delete(request,id):
   myclients=addclients.objects.get(id=id)
   myclients.delete()
   return HttpResponseRedirect(reverse('clients'))

def edit(request):
    emp=addclients.objects.all().values()
    context={
        "emp":emp,
    }
    return HttpResponseRedirect(request,'clients.html', context)
    
def update(request,id):
  a = request.POST['first']
  b = request.POST['last']
  c = request.POST['dni']
  d = request.POST['orig']
  e = request.POST['dest']
  f = request.POST['descrip']
  myclients = addclients.objects.get(id=id)
  myclients.firstname = a
  myclients.lastname = b
  myclients.dni=c
  myclients.origin=d
  myclients.destiny=e
  myclients.description=f
  myclients.save()
  return HttpResponseRedirect(reverse('clients'))

def history(request):
    myclients=addclients.objects.all().values()
    template=loader.get_template('history.html')
    context={
        'myclients':myclients,
    }
    return HttpResponse(template.render(context,request))


def filter(request):
    selectoption=request.POST['atributo']
    if selectoption=='firstname':
       a=request.POST['input_value']
       filter_name=addclients.objects.filter(firstname=a).values()
       template=loader.get_template('history.html')
       context={
        "myclients":filter_name,
       }
       return HttpResponse(template.render(context,request))

    if selectoption=='lastname':
       a=request.POST['input_value']
       filter_name=addclients.objects.filter(lastname=a).values()
       template=loader.get_template('history.html')
       context={
        "myclients":filter_name,
       }
       return HttpResponse(template.render(context,request))

    if selectoption=='dni':
       a=request.POST['input_value']
       filter_name=addclients.objects.filter(dni=a).values()
       template=loader.get_template('history.html')
       context={
        "myclients":filter_name,
       }
       return HttpResponse(template.render(context,request))






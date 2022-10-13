from pydoc import describe
from django.shortcuts import render
from .models import Detail
# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request,'home.html') 

def detail(request):
    # html=''
    values={}
    queryset= Detail.objects.all()
    # values=[{i.name : i.description} for i in queryset] 
    for i in queryset:
        values[i.name]=i.description

    # for value in values:
    #     url= '/asgardApp/' + value.name +'/'
    #     html+= '<a href="'+ url + '" >'  '</a>'

    # return HttpResponse(html)

    return render(request,'home.html' , context={'data': values})




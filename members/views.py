from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Member


# def members(request):
#     template = loader.get_template('myfirst.html')
#     return HttpResponse(template.render())

def first_page(request):
    return HttpResponse('This is the first page after starting the run server')


def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    #import pdb;pdb.set_trace()
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

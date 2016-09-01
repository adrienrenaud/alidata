# -*- coding: utf-8 -*-

import os

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.core.files.storage import default_storage
from django import forms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test

from django.contrib.auth.models import User, Group
from django.core.files.base import ContentFile


from django.template import TemplateDoesNotExist

from datetime import datetime

        
import json
import gviz_api
        
        
        
################################################
########### homepage, comptes, mail
################################################


def homepage_view(request):

    # Creating the data
    description = [('X', 'number'), ('Dogs', 'number')]
    data = [(0,2),(1,21),(2,12),(3,30)]
    options = json.dumps( { 'hAxis': { 'title': 'Time'}, 'vAxis': {'title': 'Popularity'}, 'backgroundColor': 'white'} )
    
    # Loading it into gviz_api.DataTable
    data_table = gviz_api.DataTable(description)
    data_table.LoadData(data)

    # Create a JSON string.
    gviz_data = data_table.ToJSon()
    
    argDict = {'request':request, 'gviz_data' : gviz_data, 'options':options}

    # return render_to_response('homepage.html', argDict, context_instance=RequestContext(request))
    return render(request, 'homepage.html', context=argDict)
    
    
    
    
    
def notebook_view(request):


    
    argDict = {'notebook_name': 'ana_var18.html'}

    # return render_to_response('homepage.html', argDict, context_instance=RequestContext(request))
    return render(request, 'notebook_base.html', context=argDict)
    
    
    
    
    
# def about(request):
#     argDict = {'request':request,}
#     return render_to_response('about.html', argDict, context_instance=RequestContext(request))
# def tutoriel(request):
#     argDict = {'request':request,}
#     return render_to_response('tutoriel.html', argDict, context_instance=RequestContext(request))
    
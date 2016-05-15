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



        
        
# from django.utils import simplejson
import json

   
        
        
import gviz_api
        
        
        
################################################
########### homepage, comptes, mail
################################################


def homepage_view(request):

    js_data = json.dumps({'foo':300})  

            
            
    # Creating the data
    description = [('X', 'number'), ('Dogs', 'number')]
    data = [(0,2),(1,21),(2,12),(3,30)]

    # Loading it into gviz_api.DataTable
    data_table = gviz_api.DataTable(description)
    data_table.LoadData(data)

    # Create a JSON string.
    # gviz_data = data_table.ToJSon(columns_order=("X", "Dogs"), order_by="X")
    gviz_data = data_table.ToJSon()
    
    
    
    
    # argDict = {'request':request, 'my_data' : js_data}
    argDict = {'request':request, 'my_data' : 300, 'js_data': js_data, 'gviz_data' : gviz_data}
    # argDict = {'request':request, 'foo' : {'bar':100}}
    return render_to_response('homepage.html', argDict, context_instance=RequestContext(request))
    
# def about(request):
#     argDict = {'request':request,}
#     return render_to_response('about.html', argDict, context_instance=RequestContext(request))
# def tutoriel(request):
#     argDict = {'request':request,}
#     return render_to_response('tutoriel.html', argDict, context_instance=RequestContext(request))
    
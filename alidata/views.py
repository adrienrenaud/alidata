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
from siteCoGM.apps.userdata.models import Userdata, Textfile

from django.template import TemplateDoesNotExist

from datetime import datetime
from helper_compte_pf import clean_list, compute_stuff, compute_info, print_compte, print_mail



        
        
        
        
        
        
        
        
        
################################################
########### homepage, comptes, mail
################################################


def homepage_view(request):
    argDict = {'request':request,}
    return render_to_response('homepage.html', argDict, context_instance=RequestContext(request))
    
# def about(request):
#     argDict = {'request':request,}
#     return render_to_response('about.html', argDict, context_instance=RequestContext(request))
# def tutoriel(request):
#     argDict = {'request':request,}
#     return render_to_response('tutoriel.html', argDict, context_instance=RequestContext(request))
    
# -*- coding: utf-8 -*-


from django.shortcuts import render,HttpResponse,redirect
from time import gmtime,strftime
from django.contrib import messages
from django.utils.crypto import get_random_string


def index(request):
	request.session['counter']=1
	
	return render(request,"word_random/random.html")

def create(request):
	if 'counter' in request.session:
		request.session['counter']+=1

	
	context={
			

		'unique_id': get_random_string(length=14)
	}

	return render(request,"word_random/random.html",context)


def reset(request):
	request.session.clear()
	return redirect('/')


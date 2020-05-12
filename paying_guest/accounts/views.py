from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.
from .models import *
from django.contrib.auth.decorators import login_required

def index(request):
	data = User.objects.filter(first_name='rahul')
	context = {'data' : data}
	print(context)
	return render(request,'registration/home.html',context)

def register(request):
	if request.method == 'POST':
		data = {}
		username = request.POST.get('username')
		password = request.POST.get('password')
		email =request.POST.get('email')
		first_name = request.POST.get('firstname')
		last_name = request.POST.get('lastname')
		lastname=request.POST.get('lastname')
		if(request.POST.get('firstname')):
			data['firstname']=request.POST.get('firstname')
		if (request.POST.get('lastname')):
			data['lastname'] = request.POST.get('lastname')
		if (request.POST.get('phone')):
			data['phone'] = request.POST.get('phone')
		if (request.POST.get('sex')):
			data['sex'] = request.POST.get('sex')
		user = User.objects.create(email=email,username=username,password=password,first_name=first_name,last_name=last_name)
		userdata = User.objects.filter(username=username)
		##if userdata:
		##	userid = userdata.id
		##userextra_data = UserProfile.objects.create(fieldname=fieldvalue,fieldname1=fieldvalue1,user=userid)
		userdata1 = UserProfile.objects.filter(user=user).update(**data)
		userdata = UserProfile.objects.get(user=user)
		return render(request,'registration/signup.html',{})
	else:
		return render(request, 'registration/signup.html',{})

def logout_user(request):
	logout(request)
	return redirect('login')



def login_user(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		print(user)
		if user is not None:
			login(request, user)
			return redirect("/")
		else:
			msg = 'incorrect details'
			return render(request, 'registration/login.html', {'msg': msg})
	else:
		msg = ''
		return render(request, 'registration/login.html', {'msg': msg})

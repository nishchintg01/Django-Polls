from django.shortcuts import render
from .forms import *
from .models import Poll
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django .contrib.auth.models import User

# Homepage Section
def Index(request):
	return render(request,'Home.html')

# Dashboard 
@login_required
def Surveys(request):
	UserQuestions = Poll.objects.filter(user=request.user)[::-1]
	AllQuestions = Poll.objects.all()[::-1]
	context={
	'feedbacks':UserQuestions,
	'AllQuestions':AllQuestions
	}
	return render(request,'dashboard.html',context)

# Edit Polls 
@login_required
def edit(request,id):
	model = Poll.objects.get(id=id)
	if request.method == 'POST':
		form = SurveyForm(request.POST,instance=model)
		if form.is_valid():
			form = form.save(commit=False)
			form.user = request.user
			form.save()
			return redirect('dashboard')
		else:
			context = {'form': SurveyForm(instance = model)}
			return render(request,'survey.html',context)			
	
	form = SurveyForm(instance = model)
	context ={
	'form':form
	}
	return render(request,'EditForm.html',context)


# Poll Add
@login_required
def surveyForm(request):
	if request.method == 'POST':
		form = SurveyForm(request.POST)
		if form.is_valid():
			form = form.save(commit=False)
			form.user = request.user
			form.save()
			return redirect('dashboard')
		else:
			context = {'form': SurveyForm()}
			return render(request,'survey.html',context)			
	context = {'form': SurveyForm()}
	return render(request,'survey.html',context)

# Report 
@login_required
def Report(request,id):
	data = Poll.objects.get(id=id)
	total = data.Points3 + data.Points2 + data.Points1
	if total==0:
		total=1
	one = round((data.Points1/total)*100,2)
	two = round((data.Points2/total)*100,2)
	three =  round((data.Points3/total)*100,2)
	context={
	'data':data,'one':one,'two':two,'three':three
	}
	return render(request,'report.html',context)

@login_required
def Vote(request,id):
	data = Poll.objects.get(id=id)
	if request.method=='POST':
		item = request.POST['exampleRadios']
		if item == 'Option1':
			data.Points1 +=1
		elif item == 'Option2':
			data.Points2 +=1
		else:
			data.Points3 += 1
		data.save()
		return redirect('dashboard')
	context = {
	'poll':data
	}
	return render(request,'vote.html',context)

# Authentication Functions
def LoginPage(request):
	if request.method == 'POST':
		form = Login(request.POST)
		if form.is_valid():
			username = form.cleaned_data['Username']
			password = form.cleaned_data['Password']
			user = authenticate(request,username=username,password=password)
			if user is not None:
				login(request,user)
				return redirect('dashboard')
			else:
				return redirect('LoginPage')
	else:
		form =Login()
		context ={
		'form':form
		}
	return render(request,'login.html',context)

def Signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def LogoutView(request):
	logout(request)
	return redirect('home')


from django.urls import path
from .views import *
from django.views.generic import TemplateView
urlpatterns = [
	path('survey/edit/<int:id>',edit,name='editsurvey'),
	path('',Index,name='home'),
	path('login',LoginPage,name='LoginPage'),
	path('Signup',Signup,name='signup'),
	path('Logout',LogoutView,name='logout'),
	path('dashboard',Surveys,name='dashboard'),
	path('survey',surveyForm,name='survey'),
	path('report/<int:id>',Report,name="report"),
	path('vote/<int:id>',Vote,name='vote')	
]

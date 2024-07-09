from django.shortcuts import render,redirect
from django.views import View
from .models import *

# Create your views here.

class CountryView(View):
	def get(self,request):
		countryobj = Country.objects.all()
		return render(request,'country.html',{'countryobj':countryobj})
	
	def post(self,request):
		country_name=request.POST.get('country_name')
		slug = request.POST.get('slug')
		code = request.POST.get('code')
		flag = request.FILES.get('flag')
		state_available = request.POST.get('state_available')

		Country.objects.create(name = country_name,slug = slug, 
						 code = code,flag = flag, is_state_available =state_available)
		return redirect('/')
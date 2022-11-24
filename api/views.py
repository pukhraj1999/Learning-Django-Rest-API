from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def home(req):
	return JsonResponse({"message":"Working Successfully"})
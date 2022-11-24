from django.shortcuts import render
from django.http import JsonResponse
import json
from products.models import Product

# Create your views here.
def home(req):
	model_data=Product.objects.all().order_by("?").first() #getting products randomly
	data={}
	#Adding model data if available
	if model_data:
		data['id']=model_data.id #comes by default
		data['title']=model_data.title
		data['content']=model_data.content
		data['price']=model_data.price
	return JsonResponse({"message":"Working Successfully","data":data})
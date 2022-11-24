from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.
def home(req):
	#using req.body
	body=req.body #byte string of json data
	data={} #data from front end as json
	try:
		data=json.loads(body) #converting json to python dictionary
	except:
		pass
	
	data['headers']=dict(req.headers) #converting headers to dictionary
	data['content_type']=req.content_type
	data['params']=dict(req.GET)
	return JsonResponse({"message":"Working Successfully","postData":data})
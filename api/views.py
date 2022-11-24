from django.http import JsonResponse
from products.models import Product
#from django.forms.models import model_to_dict

from rest_framework.response import Response

# Create your views here.
def home(req):
	model_data=Product.objects.all().order_by("?").first() #getting products randomly
	data={}
	#Adding model data if available
	if model_data:
		data=model_to_dict(model_data,fields=['id','title','content'])
	return JsonResponse({"message":"Working Successfully","data":data})
from django.forms.models import model_to_dict

from products.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','POST']) #this decorator allows only methods defined by us
def home(req):
	model_data=Product.objects.all().order_by("?").first() #getting products randomly
	data={}
	#Adding model data if available
	if model_data:
		data=model_to_dict(model_data,fields=['id','title','content'])
	return Response({"message":"Working Successfully","data":data},status=200)
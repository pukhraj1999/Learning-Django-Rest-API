#from django.forms.models import model_to_dict

from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET']) #this decorator allows only methods defined by us
def home(req):
	instance=Product.objects.all().order_by("?").first() #getting products randomly
	data={}
	#Adding model data if available
	if instance:
		#data=model_to_dict(model_data,fields=['id','title','content'])
		data=ProductSerializer(instance).data #Do the same above thing
	return Response({"message":"Working Successfully","data":data},status=200)

@api_view(['POST'])
def about(req):
		serializer=ProductSerializer(data=req.data)
		if serializer.is_valid(raise_exception=True): #check whether according to serializers field
			print(serializer.data)
			data=serializer.data
			return Response(data)
		return Response({"Invalid data":"Problem in parsing about"},status=400)
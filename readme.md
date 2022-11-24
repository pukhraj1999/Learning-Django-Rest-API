# Django Commands

1. `django-admin startproject <projectName> `
   [create django project]
2. `python manage.py startapp <appName>`
   [create apps inside djangoProject]
3. `python manage.py runserver <port>`
   [run server (port is optional here)]
4. `python manage.py makemigrations`
   [creating database of models]
5. `python manage.py migrate`
   [sending migrations to admin panel]
6. `python manage.py shell`
   [To use shell for inserting data in models]
7. `python manage.py createsuperuser`
   [Create superuser for admin pannel]

# Register app to settings.py

Now add app in the installed array of settings.py file inside **_projectName_** folder.

## Create a view inside views.py file of **_api_**

```py
from django.http import JsonResponse
def home(req):
	return JsonResponse({"message":"Working Successfully"})
```

## Create urls.py inside **_api_**

```py
from django.urls import path

from . import views

urlpatterns=[
	path("",views.home)
]
```

## Adding path of app inside urls.py of **_Learning_**

```py
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
]
```

## Passing json data as post from client and converting it into python dictionary in django for using it.

### Inside client.py file

```py
import requests

endpoint="http://localhost:8000/api/"

get_response=requests.get(endpoint,params={"abc":123},json={"query":"Hello Django!!"})
print(get_response.json())
```

### Inside views.py of **_api_** used for retrieving client data

```py
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

	print(data.keys())
	return JsonResponse({"message":"Working Successfully","postData":data})
```

## Passing Headers and content-type to front end inside views.py of **_api_**

```py
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
```

# Working with Models

## Create a Product model inside models.py of products app

```py
from django.db import models

# Create your models here.
class Product(models.Model):
	title=models.CharField(max_length=120)
	content=models.TextField(blank=True,null=True)
	price=models.DecimalField(max_digits=15,decimal_places=2,default=99.99)

	#using title as field to show on admin
	def __str__(self):
		return self.title

```

Now Make migrations using `python manage.py makemigrations` command and then complete it with `python manage.py migrate` to use your models

## To add data to Product model using shell use python manage.py shell command and then type below things

```shell
>>> from products.models import Product
>>> Product.objects.create(title="Hello shell!!",content="Let's do it",price=0.00)
<Product: Hello shell!!>
>>> Product.objects.create(title="Hello Django!!",content="Let's do it",price=90.00)
<Product: Hello Django!!>
>>> Product.objects.all()
<QuerySet [<Product: Hello shell!!>, <Product: Hello Django!!>]>
>>> Product.objects.all().order_by("?").first()
<Product: Hello Django!!>
```

Product.objects.all() gives all data and Product.objects.all().order_by("?").first() gives random data

## Recieving data from product database using views.py file of api

```py
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
```

Here Serialization Take place in which model instance (model_data) is taken and convert it into a python dictionary and return json to the client.

### Python way of doing serialization

```py
from products.models import Product
from django.forms.models import model_to_dict

# Create your views here.
def home(req):
	model_data=Product.objects.all().order_by("?").first() #getting products randomly
	data={}
	#Adding model data if available
	if model_data:
		data=model_to_dict(model_data,fields=['id','title','content']) #filed is optional (gives all if not mentioned)
	return JsonResponse({"message":"Working Successfully","data":data})
```

model_to_dic(anyModel) => function convert any model to dictionary from json

# Installing Rest Framework of django

Inside terminal type below command...

```
pip install djangorestframework
```

Add `rest_framework` to the `INSTALLED_APPS` setting inside Learning

```py
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

## Using Decorator **_@api_view([Methods])_** and **_Response_** from **_rest_framework_** inside **_views.py_** of **_api_**

```py
from django.forms.models import model_to_dict

from products.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET']) #this decorator allows only methods defined by us
def home(req):
	model_data=Product.objects.all().order_by("?").first() #getting products randomly
	data={}
	#Adding model data if available
	if model_data:
		data=model_to_dict(model_data,fields=['id','title','content'])
	return Response({"message":"Working Successfully","data":data},status=200)
```

## Adding **_sales_price_** property to model using **_@property_** decorator in **_models.py_** of **_product_**

```py
from django.db import models

# Create your models here.
class Product(models.Model):
	title=models.CharField(max_length=120)
	content=models.TextField(blank=True,null=True)
	price=models.DecimalField(max_digits=15,decimal_places=2,default=99.99)

	@property
	def sale_price(self): #add 80% discount
		return '%.2f' % (float(self.price)*0.8)

	@property
	def getDiscount(self):
		return "80%"

	#using title as field to show on admin
	def __str__(self):
		return self.title
```

# Using serializers of rest_framework in place of model_to_data for serializing

**`Note:-` Serializers are very similar to forms**

Inside `forms.py` of `product`,forms looks like this...

```py
from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
	class Meta:
		model=Product
		fields=[
			'title',
			'content',
			'price'
		]
```

Inside `serializers.py` of `product`,serializers looks like this...

```py
from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
	#for changing getDiscount property name
	discount=serializers.SerializerMethodField(read_only=True)
	class Meta:
		model=Product
		fields=[
			'title',
			'content',
			'price',
			'sale_price',
			'discount'
		]

	#telling serializer what discount property means
	#obj contains instance of data
	def get_discount(self,obj):
		try:
			return obj.getDiscount
		except:
			return None
```

## In order to post the data do this in **_client.py_** file

```py
import requests

endpoint="http://localhost:8000/api/about/"

get_response=requests.post(endpoint,json={"title":"Hello Love!!"})
print(get_response.status_code)
print(get_response.text)
```

## Create a about function in **_views.py_** file of api for posting data

```py
@api_view(['POST'])
def about(req):
		serializer=ProductSerializer(data=req.data)
		if serializer.is_valid(raise_exception=True): #check whether according to serializers field
			print(serializer.data)
			data=serializer.data
			return Response(data)
		return Response({"Invalid data":"Problem in parsing about"},status=400)
```

It first matches the requirements of serializers and then the request of models.Raise Exception let's the client know what the problem is.

## Now register this in **_urls.py_** file of api

```py
from django.urls import path

from . import views

urlpatterns=[
	path("",views.home),
	path("about/",views.about)
]
```

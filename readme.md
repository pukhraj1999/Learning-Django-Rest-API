# Django Commands

1. django-admin startproject **projectName**
   [create django project]
2. python manage.py startapp **appName**
   [create apps inside djangoProject]
3. python manage.py runserver **port**
   [run server (port is optional here)]
4. python manage.py makemigrations
   [creating database of models]
5. python manage.py migrate
   [sending migrations to admin panel]
6. python manage.py shell
   [To use shell for inserting data in models]

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

Now Make migrations using python manage.py makemigrations command and then complete it with python manage.py migrate to use your models

## To add data to Product model using shell use python manage.py shell command and then type below things

```shell
>>> from products.models import Product
>>> Product.objects.create(title="Hello shell!!",content="Let's do it",price=0.00)
<Product: Hello shell!!>
>>> Product.objects.create(title="Hello Django!!",content="Let's do it",price=90.00)
<Product: Hello Django!!>
```

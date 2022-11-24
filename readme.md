### Django Commands

1. django-admin startproject **projectName**
   [create django project]
2. python manage.py startapp **appName**
   [create apps inside djangoProject]
3. python manage.py runserver **port**
   [run server (port is optional here)]

## Register app to settings.py

Now add app in the installed array of settings.py file inside **_projectName_** folder.

## Create a view inside views.py file of **_appName_**

```py
from django.http import JsonResponse
def home(req):
	return JsonResponse({"message":"Working Successfully"})
```

## Create urls.py inside **_appName_**

```py
from django.urls import path

from . import views

urlpatterns=[
	path("",views.home)
]
```

## Adding path of app inside urls.py of **_projectName_**

```py
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
]
```

## Passing json data as post from client and converting it into python dictionary in django for using it.

### Inside client.py file using for post

```py
import requests

endpoint="http://localhost:8000/api/"

get_response=requests.get(endpoint,params={"abc":123},json={"query":"Hello Django!!"})
print(get_response.json())
```

### Inside views.py of **_appName_** used for retrieving client data

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
	return JsonResponse({"message":"Working Successfully"})
```

## Django Commands

1. django-admin startproject <projectName>
   [create django project]
2. python manage.py startapp <appName>
   [create apps inside djangoProject]
3. python manage.py runserver <port>
   [run server (port is optional here)]

## Register app to settings.py

Now add app in the installed array of settings.py file inside <projectName> folder.

## Create a view inside views.py file of <appName>

```
from django.http import JsonResponse
def home(req):
	return JsonResponse({"message":"Working Successfully"})
```

## Create urls.py inside <appName>

```
from django.urls import path

from . import views

urlpatterns=[
	path("",views.home)
]
```

## adding path of app inside urls.py of <projectName>

```
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
]
```

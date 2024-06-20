# Django

## Django Project Commands

### Create Django Project

```
django-admin startproject <ProjectName>
```

### Create super user

```
python manage.py createsuperuser
```

### Create migrations 

```
python manage.py makemigrations
```

### Apply migrations

```
python manage.py migrate
```

### Run server

```
python manage.py runserver
```

## Django App Commands

### Create Django App

```
python manage.py startapp <AppName>
```

## Media Settings

Add this lines into your project settings.py files

``` python
import os

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

In your project url.py file import settings and static as shown below.

```python
from django.conf import settings
from django.conf.urls.static import static
```

And add this line at the end of the url patterns array

```python
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

Now url.py looks like this.

``` python
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # ..
    # ..
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## Template Settings

Add "templates" into TEMPLATES section DIRS array.

``` python
'DIRS': ["templates"],
```
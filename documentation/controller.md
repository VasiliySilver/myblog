## Controller for main page

---
1. create urls.py in blog

```python
from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home')
]
```
2. create views handler

```python
   from django.http import HttpResponse

    def index(request):
        return HttpResponse('<h1>Привет мир<h1>')
```
4. add to projects urls.py path to blog.url

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
```
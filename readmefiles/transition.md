## Transition template to the project

1. Add index.html to blog/templates/blog
2. blog/views.py add render function to get template
```python
def index(request):
    return render(request, 'blog/index.html')
```
3. Add base.html to templates
4. Create static directory in dartblog project
5. Add our static files in dartblog/static
6. Add path to templates in settings.py TEMPLATES `os.path.join(BASE_DIR, 'templates')`   
 ```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
8. And
```python
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'dartblog/static')
]
```
7. `python manage.py collectstatic`
8. Then add our template to base.html and load static in the begining of our page `{% load static %}`
9. After that devide template for header footer and block content

```html
<header class="header">...</header>

        {% block content %}{% endblock %}

<footer class="footer">...</footer>
```
10. block content will be our index.html file
```python
{% extends 'base.html' %}

{% load static %}

{% block content %}
... OUR CONTENT ...
{% endblock %}
```
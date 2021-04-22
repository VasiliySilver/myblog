## Tag template menu

---
1. Create templates/inc/_footer.py
2. Create templates/inc/_header.py
3. Add links in base.html
```pythonverboseregexp
{% include 'inc/_header.html' %}
{% include 'inc/_footer.html' %}
```
4. views.py Get category template
```python
def get_category(request, slug):
    return render(request, 'blog/category.html')
```
5. Create templates category.html

6. add dartblog/urls.py
```python
path('category/<str:slug>', get_category, name='category')
```

7. copy index.html code into category.html

8. Create blog/templatetags/__init__.py
9. Create blog/templatetags/menu.py
```python
from django import template
from blog.models import Category

register = template.Library()

@register.inclusion_tag('blog/menu_tpl.html')
def show_menu(menu_class='menu'):
    categories = Category.objects.all()
    return {"categories": categories, "menu_class": menu_class}
```

10. Create menu_tpl.html template
```html
<div class="{{ menu_class }}">
    <ul>
        <li><a href="{% url 'home' %}">Home</a></li>
        {% for item in categories %}
            <li><a href="{{ item.get_absolute_url }}">{{ item.title }}</a></li>
        {% endfor %}
    </ul>
</div>
```
11. Add tag in _header.html and _footer.html
- **_header.html**
```html
<div class="col-md-10">
    {% show_menu %}
</div>
```
- **_footer.html**
```html
<div class="col-md-9">
{% show_menu 'footer-menu' %}
<!--{# <ul>#}-->
<!--{#     <li class="active"><a href="#">Home</a></li>#}-->
<!--{#     <li><a href="#">lifestyle</a></li>#}-->
<!--{#     <li><a href="#">Food</a></li>#}-->
<!--{#     <li><a href="#">Nature</a></li>#}-->
<!--{#     <li><a href="#">photography</a></li>#}-->
<!--{# </ul>#}-->
</div>
```

12. Add caches
[Система кеширования](https://djbook.ru/rel1.5/topics/cache.html)

```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'django_cache'),
    }
}
```

13. Add cache for repeating tag menu
```python
{% cache 20 header %}
{% include 'inc/_header.html' %}
{% endcache %}

{% block content %}{% endblock %}

{% cache 20 footer %}
{% include 'inc/_footer.html' %}
{% endcache %}
```


## Displaying articles on the main

---

1. Add Home view in views.py for home page
```python
class Home(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Classic Blog Design'
        return context
```

2. change blog/urls.py from index to Home.as_view()

![img_2.png](img/urls/2.png)

3. add title block

```python
{% block title %}{{ title }} :: {{ block.super }}  {% endblock %}
```

- where title we get from context 

4. models.py - get absolut url for post
```python
class Post:
    ...
def get_absolute_url(self):
        return reverse('post', kwargs={"slug": self.slug})
```
- url for post urls.py
```python
path('post/<str:slug>/', get_post, name='post')
```
5. Select the post block and display posts through a loop

```html
{% for post in posts %}
<div class="col-md-3">
    <div class="single-post">

        {% if post.photo %}
            <img src="{% static 'img/post-image2.jpg'%}" alt="{{ post.title }}">
        {% else %}
            <img src="https://i.picsum.photos/id/1000/300/201.jpg?hmac=qWh065Fr_M8Oa3sNsdDL8ngWXv2Jb-EE49ZIn6c0P-g" alt="{{ post.title }}">
        {% endif %}

        <h3><a href="{{ post.get_absolute_url }}">{{ post.title}}</a></h3>
        <h4><span>Posted By: <span class="author-name">{{ post.author }}</span></span>
        </h4>
        <p>{{ post.content|truncatewords_html:20|striptags }}</p>
        <h4><span>{{ post.created_at|date:"d/m/Y" }}</span></h4>
    </div>
</div>
{% endfor %}
```

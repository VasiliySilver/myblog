## Show posts for tag

---

1. Change in views.py get_post on class GetPost
```python
class GetPost(DetailView):
    model = Post
    template_name = 'blog/single.html'
    context_object_name = 'post'
```

2. add blog/single.html

3. change path to `path('post/<str:slug>/', GetPost.as_view(), name='post'),`

4. Add get context data for GetPost
```python
 def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        # Кол-во просмотров
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db() # помогает обновлять значения из бд
        return context
```

5. single.html

```html
<h2>{{ post.title }}</h2>
<div class="single-content">
    <div>
        <span>Category: <a href="{{ post.category.get_absolute_url }}">{{ post.category }}</a></span>
        <br>
        {% if post.tags.exists %}
        <span>
            Tags:
            {% for tag in post.tags.all %}
            <a href="{{ tag.get_absolute_url }}">{{ tag.title }}</a>
            {% endfor %}
        </span>
        <br>
        {% endif %}
        <span>Views: {{ post.views }}</span>
    </div>
    {{ post.content|striptags }}
</div>
```
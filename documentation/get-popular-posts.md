## get-popular-posts
[TOC]
### Get popular posts
- sidebar.py

- handler for popular posts
- popular_posts_tpl.html
```python
from django import template
from blog.models import Post, Tag

register = template.Library()

@register.inclusion_tag('blog/popular_posts_tpl.html')
def get_popular(cnt=3):
    posts = Post.objects.order_by('-views')[:cnt]
    return {"posts": posts}
```
### create popular_posts_tpl.html
- create representation of popular posts
- popular_posts_tpl.html
```html
<h2 class="sidebar-title">Popular posts</h2>
<div class="grid">
    {% for post in posts %}
        <div class="portfolio-item popular">
            {% if post.photo %}
                <img src="{{ post.photo.url }}" alt="{{ post.title }}">
            {% elif p > page_obj.number|add:-3 and p < page_obj.number|add:3 %}
                <img src="https://i.picsum.photos/id/1000/300/201.jpg?hmac=qWh065Fr_M8Oa3sNsdDL8ngWXv2Jb-EE49ZIn6c0P-g"
                     alt="{{ post.title }}">
            {% endif %}

            <div class="portfolio-text">
                <h5><a href="{{ post.get_absolute_url }}">{{ post.title }}</a></h5>
                <p>{{ post.author }}<span>|</span>{{ post.created_at|date:"d/m/Y" }}</p>
            </div>
        </div>
    {% endfor %}
</div>
```
### fix style for photo popular posts
- fix representation popular posts
- style.css
```css
.single-blog-area .tags p a {
    color: #fff;
    display: inline-block;
    text-decoration: none;
}
```
### get absolute url for posts
- return absolute url for posts
- models.py
```py
    def get_absolute_url(self):
        return reverse('post', kwargs={"slug": self.slug})
```
